pipeline {
    agent any

    stages {

        stage('Check Docker') {
            steps {
                sh 'docker ps'
            }
        }

        stage('Check Kubernetes') {
            steps {
                sh 'kubectl get pods'
            }
        }

        stage('Deployment Successful') {
            steps {
                echo 'Pipeline executed successfully'
            }
        }
    }
}