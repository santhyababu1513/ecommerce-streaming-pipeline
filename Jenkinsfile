pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Check Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }
}