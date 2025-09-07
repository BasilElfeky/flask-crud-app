pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/BasilElfeky/flask-crud-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app-flask-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop flask-crud || true'
                sh 'docker rm flask-crud || true'
                sh 'docker run -d --name flask-crud -p 5000:5000 flask-app-flask-app'
            }
        }
    }
}

