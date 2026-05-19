pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'docker build -t myapp-test -f Dockerfile.test .'
                sh 'docker run --rm myapp-test'
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
