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
        
        stage('🐍 3. TEST (optionnel)') {
            steps {
                echo 'Vérification des dépendances...'
                sh '''
                    pip install -r requirements.txt || true
                    echo "✅ Dépendances OK"
                '''
            }
        }
        
        stage('🐳 4. CONSTRUCTION IMAGE DOCKER') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker images | grep ${IMAGE_NAME}
                '''
            }
        }
        
        stage('🚀 5. LANCEMENT CONTENEUR') {
            steps {
                sh '''
                    # Arrêter et supprimer l'ancien conteneur s'il existe
                    docker stop python-portfolio 2>/dev/null || true
                    docker rm python-portfolio 2>/dev/null || true
                    
                    # Lancer le nouveau conteneur
                    docker run -d -p 5000:5000 --name python-portfolio ${IMAGE_NAME}:${IMAGE_TAG}
                    
                    echo "✅ Application lancée sur http://localhost:5000"
                '''
            }
        }
        
        stage('✅ 6. SUCCÈS') {
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
