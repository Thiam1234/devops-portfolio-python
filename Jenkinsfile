pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "moustapha-python"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('📥 1. RÉCUPÉRATION CODE') {
            steps {
                echo 'Récupération du code depuis GitHub...'
                checkout scm
            }
        }
        
        stage('📝 2. INFORMATIONS') {
            steps {
                sh '''
                    echo "Build numéro: ${BUILD_NUMBER}"
                    echo "Révision Git: ${GIT_COMMIT}"
                    ls -la
                '''
            }
        }
        
        stage('🐳 3. CONSTRUCTION IMAGE DOCKER') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                    docker images | grep ${IMAGE_NAME}
                '''
            }
        }
        
        stage('🚀 4. LANCEMENT CONTENEUR (TEST LOCAL)') {
            steps {
                sh '''
                    # Arrêter et supprimer l'ancien conteneur
                    docker stop python-portfolio 2>/dev/null || true
                    docker rm python-portfolio 2>/dev/null || true
                    
                    # Lancer le nouveau conteneur
                    docker run -d -p 5000:5000 --name python-portfolio ${IMAGE_NAME}:${IMAGE_TAG}
                    
                    # Attendre que l'app démarre
                    sleep 3
                    
                    # Tester que l'app répond
                    curl -s http://localhost:5000 | grep -q "Moustapha" && echo "✅ Application OK" || echo "⚠️ Vérifie l'app"
                    
                    echo "🌍 http://localhost:5000"
                '''
            }
        }
        
        stage('✅ 5. SUCCÈS') {
            steps {
                echo '═══════════════════════════════════'
                echo '🎉 APPLICATION PYTHON PRÊTE !'
                echo '═══════════════════════════════════'
                echo ''
                echo "📦 Image : ${IMAGE_NAME}:${IMAGE_TAG}"
                echo "🌍 Accès : http://localhost:5000"
                echo "📂 Code : https://github.com/Thiam1234/devops-portfolio-python"
            }
        }
    }
    
    post {
        failure {
            echo '❌ Le pipeline a échoué. Vérifie les logs.'
        }
    }
}
