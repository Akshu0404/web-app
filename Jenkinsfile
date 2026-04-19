pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting application...'
                bat 'nohup python app.py &'
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
        always {
            cleanWs()
        }
    }
}
