pipeline {
    agent any
    
    environment {
        // Define environment variables
        DOCKER_IMAGE = 'shahgulse/firstrepo' // Replace with your Docker Hub repo name
        DOCKER_TAG = 'latest' // You can also use ${env.BUILD_NUMBER} to use Jenkins build number
        // Use the Jenkins Credentials Binding plugin to inject credentials
        //DOCKER_CREDENTIALS = credentials('docker-hub-credentials') // Replace with the ID of your Docker Hub credentials in Jenkins
    }

    stages {

stage('Checkout Code') {
            steps {
                // Clone the GitHub repository
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh 'echo $DOCKERHUB_PASS | docker login --username $DOCKERHUB_USER --password-stdin'
                    }
                    // Build the Docker image
                    sh "docker build -t ${env.DOCKER_IMAGE}:${env.DOCKER_TAG} ."
                    sh "pwd"
                    sh "docker ps -a"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh "docker push ${env.DOCKER_IMAGE}:${env.DOCKER_TAG}"
                }
            }
        }

        // If you need to run the container, uncomment the following stage
        stage('Run Docker Container') {
            steps {
                // Run the Docker container
                sh "docker stop my-blog-app"
                sh "docker ps -a"
                sh "docker start my-blog-app"
               

                
                sh "docker run -p 5000:5000 --name my-blog-app ${env.DOCKER_IMAGE}:${env.DOCKER_TAG}"
                 sh "docker logs my-blog-app"
                sh "docker stop my-blog-app"
		sh "docker rm my-blog-app"
            }
        }
        
    }

    post {
        always {
            // Logout from Docker Hub
            sh 'docker logout'
            // Clean up the workspace
            cleanWs()
        }
    }
}
