pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // This step checks out your source code from your version control system (e.g., Git)
                script {
                    checkout scm
                }
            }
        }
        
        stage('Build') {
            steps {
                // This step executes the build process
                script {
                    sh 'mvn clean package' // Example for Maven build
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    sh 'mvn test' // Example for Maven test
                }
            }
        }
        
        stage('Deploy') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    sh 'kubectl apply -f deployment.yaml' // Example for Kubernetes deployment
                }
            }
        }
    }
    
    post {
        failure {
            mail to: 'cyrilmuchiri11@gmail.com',
                 subject: 'Failed Pipeline: ${currentBuild.fullDisplayName}',
                 body: "Something is wrong with ${env.JOB_NAME} build ${env.BUILD_NUMBER}"
        }
    }
}
