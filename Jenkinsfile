pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKER_COMPOSE_VERSION = '3.8'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the GitHub repository
                checkout scm
            }
        }
        stage('Run Docker Compose') {
            steps {
                script {
                    // Login to Docker Hub if needed
                    // sh 'echo $DOCKERHUB_PASS | docker login --username $DOCKERHUB_USER --password-stdin'
                    
                    // Start the application using Docker Compose
                    sh 'docker-compose up -d'
               
                }
            }
        }
        stage('Verify Deployment') {
            steps {
                script {
                    // Verify if the application is running correctly
                    sh 'docker-compose ps'
                    sh 'docker-compose logs web'
                    sh 'docker logs flask-container'
                }
            }
        }
    }

    post {
        always {
            // Clean up: stop and remove docker containers and networks
            sh 'docker-compose down'
            
            // Logout from Docker Hub if you logged in before
            // sh 'docker logout'
            
            // Clean up the workspace
            cleanWs()
        }
    }
}

