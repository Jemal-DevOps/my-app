pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'docker run --rm -v $(pwd):/app -w /app python:3.12-slim sh -c "pip install -r requirements.txt -q && pytest tests/ -v"'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t myapp:${BUILD_NUMBER} .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop myapp-running || true'
                sh 'docker rm myapp-running || true'
                sh 'docker run -d --name myapp-running -p 5000:5000 myapp:${BUILD_NUMBER}'
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded — app deployed' }
        failure { echo 'Pipeline failed — check logs above' }
    }
}
