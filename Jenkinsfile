pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'docker-compose build'
                sh 'python3 --version'
            }
        }
        stage('test') {
            steps {
                sh 'pwd'
                sh 'python3 -m venv env && . env/bin/activate'
                //sh 'pytest'
            }
        }
        stage('package') {
            steps {
                sh 'python3 --version'
                
            }
        }
    }
}
