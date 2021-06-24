pipeline {
    agent any
    stages {
        stage('setup') {
            steps {
                sh 'docker pull python:3.7.3-alpine'
                sh 'python --version'
            }
        }
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test') {
            steps {
                sh 'python --version'
            }
        }
        stage('package') {
            steps {
                sh 'pytest'
            }
        }
    }
}
