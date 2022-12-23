pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('List Files') {
            steps {
                script {
                    sh 'ls -R'
                }
            }
        }
    }

    post {
        always {
            echo 'Job completed'
        }
    }
}
