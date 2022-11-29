pipeline { 
    agent { label 'linux'}
    stages { 
        stage('git clone'){
            steps { 
                git branch: 'main', url: 'https://github.com/AlmogChn/Tsunami.git'
            }
        }
        stage('Create List') {
            steps {
                script {
                    list = ["127.0.0.1" , "77.125.40.74" , "77.137.66.24", "3.127.66.246"]
                }
            }
        }
        stage('Dynamic Stages') {
            steps {
                script {
                    for(int i=0; i < list.size() ; i++) {
                        stage("scan ${list[i]}"){
                        sh "cd /home/ubuntu/tsunami && \
                            java -cp 'tsunami-main-0.0.15-SNAPSHOT-cli.jar:/home/ubuntu/tsunami/plugins/*' \
                            -Dtsunami-config.location=/home/ubuntu/tsunami/tsunami.yaml \
                            com.google.tsunami.main.cli.TsunamiCli \
                            --ip-v4-target=${list[i]} \
                            --scan-results-local-output-format=JSON \
                            --scan-results-local-output-filename=/tmp/tsunami-output.json " 
                              sh 'python3 shortreport.py'
                        }
                        stage("Short scan report ${list[i]}") {
                            sh 'python3 shortreport.py'
                        }
                        stage("Full scan report ${list[i]}"){
                            sh 'less /tmp/tsunami-output.json' 
                        }
                    }
                }
            }
        }
    }  
}
