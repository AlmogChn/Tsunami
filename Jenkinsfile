pipeline { 
    agent { label 'linux'}
    stages { 
        stage('git clone'){
            steps { 
                sh 'git clone https://github.com/AlmogChn/Tsunami.git'
            }
        }
        stage('docker compose'){
            steps {
                sh ' sudo docker  compose -f /Tsunami/docker-compose.yml up -d'
            }
        }        
    }  
    post {
        always {
            sh "sudo rm -r Tsunami"
        }
    }
}

