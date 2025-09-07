pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app-flask-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          doGenerateSubmoduleConfigurations: false, 
                          extensions: [], 
                          userRemoteConfigs: [[
                              url: 'https://github.com/BasilElfeky/flask-crud-app.git', 
                              credentialsId: 'github-token'
                          ]]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker stop ${DOCKER_IMAGE} || true
                    docker rm ${DOCKER_IMAGE} || true
                    docker run -d -p 5000:5000 --name ${DOCKER_IMAGE} ${DOCKER_IMAGE}
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Flask app is running on port 5000.'
        }
        failure {
            echo 'Pipeline failed! Check the logs.'
        }
    }
}


