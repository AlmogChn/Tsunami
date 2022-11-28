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
                sh ' sudo docker compose -f /Tsunami/docker-compose.yml up -d'
            }
        }
        stage('Tsunami scan'){
            steps {
                sh  'cd /home/ubuntu/tsunami && \
                    java -cp "tsunami-main-0.0.15-SNAPSHOT-cli.jar:/home/ubuntu/tsunami/plugins/*" \
                    -Dtsunami-config.location=/home/ubuntu/tsunami/tsunami.yaml \
                    com.google.tsunami.main.cli.TsunamiCli \
                    --ip-v4-target=127.0.0.1 \
                    --scan-results-local-output-format=JSON \
                    --scan-results-local-output-filename=/tmp/tsunami-output.json' 
            }
        }        
        stage('PortScanReport'){
            steps {
                sh 'less /tmp/tsunami-output.json'
            }
        } 
    }  
    post {
        always {
            sh 'docker stop $(docker ps -a -q)'
            sh 'docker rm $(docker ps -a -q)'
            sh 'docker rmi $(docker ps -a -q)'
        }
    }
}
