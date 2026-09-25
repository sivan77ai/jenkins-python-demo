// Declarative pipeline - used from Module 5 onwards.
// Ignore this file while you are doing the freestyle-job modules.
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Building ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                sh 'ls -la'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --quiet --upgrade pip
                    pip install --quiet -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --junitxml=test-results/results.xml -v
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results/*.xml'
        }
        success {
            echo 'All tests passed.'
        }
        failure {
            echo 'Build failed - check the test report.'
        }
    }
}
