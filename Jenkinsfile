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
                sh 'apt-get install python3-venv -y'
                sh 'python3 -m venv env && . .env/bin/activate && python3 -m pip install pytest'
                sh 'pytest'
            }
        }
        stage('package') {
            steps {
                sh 'python3 --version'
                
            }
        }
    }
}
