pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building ABC Bank application...'
            }
        }

        stage('Test') {
            steps {
             sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying ABC Bank application...'
            }
        }
    }
}
