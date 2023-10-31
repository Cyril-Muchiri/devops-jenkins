pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                }
            }
        }
    }
    
    post {
        always {
            junit 'target/surefire-reports/**/*.xml'
        }
        
        success {
            echo 'Build and tests passed!'
        }
        
        failure {
            echo 'Build or tests failed!'
        }
    }
}
