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
        
        stage('🐳 2. CONSTRUCTION IMAGE DOCKER') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                    docker images | grep ${IMAGE_NAME}
                '''
            }
        }
        
        stage('🚀 3. LANCEMENT DU CONTENEUR') {
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
                    echo "✅ Application lancée sur http://localhost:5000"
                    curl -s http://localhost:5000 | grep -o "Moustapha" || echo "⚠️ Vérifie l'app"
                '''
            }
        }
        
        stage('✅ 4. SUCCÈS') {
            steps {
                echo '═══════════════════════════════════'
                echo '🎉 APPLICATION PYTHON DÉPLOYÉE !'
                echo '═══════════════════════════════════'
                echo ''
                echo "🌍 Accès : http://localhost:5000"
                echo "📦 Image : ${IMAGE_NAME}:${IMAGE_TAG}"
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
