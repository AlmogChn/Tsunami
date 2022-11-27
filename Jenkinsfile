pipeline { 
    agent { label 'linux'}
    stages { 
        stage('git clone'){
            steps { 
                git branch: 'main', url: 'https://github.com/AlmogChn/Tsunami.git'
            }
        }
        stage('docker compose'){
            steps {
                sh 'docker-compose up -d'
            }
        }
    }  
}
