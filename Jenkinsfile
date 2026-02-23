pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "moustapha-python"
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY = "localhost:32000"
    }
    
    stages {
        stage('📥 1. RÉCUPÉRATION CODE') {
            steps {
                checkout scm
            }
        }
        
        stage('🐳 2. CONSTRUCTION IMAGE DOCKER') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('📤 3. POUSSER VERS REGISTRE') {
            steps {
                sh '''
                    docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${REGISTRY}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('☸️ 4. DÉPLOIEMENT KUBERNETES') {
            steps {
                sh '''
                    # Mettre à jour l'image dans le fichier de déploiement
                    sed -i "s|image:.*|image: ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}|" k8s-deployment.yaml
                    
                    # Appliquer le déploiement
                    microk8s kubectl apply -f k8s-deployment.yaml
                    
                    # Attendre que les pods soient prêts
                    sleep 5
                    microk8s kubectl get pods
                '''
            }
        }
        
        stage('✅ 5. VÉRIFICATION') {
            steps {
                sh '''
                    echo "📦 Pods :"
                    microk8s kubectl get pods
                    echo ""
                    echo "🌍 Service :"
                    microk8s kubectl get svc python-portfolio-service
                    echo ""
                    echo "🚀 Application accessible sur : http://192.168.56.1:31000"
                '''
            }
        }
    }
}
