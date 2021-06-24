pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'docker-compose up --build'
                sh 'python3 --version'
            }
        }
        stage('test') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('package') {
            steps {
                sh 'pytest'
            }
        }
    }
}
