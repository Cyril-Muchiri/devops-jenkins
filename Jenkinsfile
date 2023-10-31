pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // This step checks out your source code from your version control system (e.g., Git)
                    checkout scm
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // This step executes the build process
                    sh 'mvn clean package' // Maven build
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // This step executes your tests
                    sh 'mvn test' // Maven test
                }
            }
        }
    }
    
    post {
        always {
            // This block is executed after all stages, regardless of success or failure
            junit 'target/surefire-reports/**/*.xml' // Publish JUnit test results
        }
        
        success {
            // This block is executed if all stages are successful
            echo 'Build and tests passed!'
        }
        
        failure {
            // This block is executed if any of the stages fail
            echo 'Build or tests failed!'
        }
    }
}
