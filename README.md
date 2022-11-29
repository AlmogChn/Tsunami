# Tsunami
Tsunami is a general purpose network security scanner with an extensible plugin
system for detecting high severity vulnerabilities with high confidence.

# The purpose of the scanner in the organization
We would like to know if there are any vulnerabilities in our organization's servers which are stored in a list. We have an additional server on which the Tsunami scanner is installed(aws, ec2).

# Operating Instructions
* Prior to running the scanner, contact me for turning on the EC2 server where tsunami is installed on.


1. **Jenkins** -> Manage nodes and clouds -> New node -> "linux" (name):             ## Guide to adding a Node for SSH access to AWS

     a. Name : 'linux'
     
     b. Remote root directory :' /home/ubuntu '
     
     c. Labels : 'linux'
     
     d. Usage : 'Only build jobs with label expressions matching this node'
     
     e. Launch method : 'launch agents via ssh'
     
     f. Host :  *Ask me directly after I turn on the server
     
     g. Credentials -> add -> Credentials -> kind : 'ssh username with private key' , ID&Description : 'ubunto', Private Key : *paste the content from .pem that i sent         in a separate email  
     
     h. Tool Locations -> home :' /usr/bin/git' ##for work with git
     
     i. Save
     
     
     
     
2. **Jenkins** -> New pipeline project -> :   #build the pipeline

     a. Build Triggers : ' GitHub hook trigger for GITScm polling '
     
     b. Pipeline - > Definition : ' Pipeline script from SCM  ' 
     
     c. SCM : ' Git '
     
     d. Repository URL : ' https://github.com/AlmogChn/Tsunami.git '
     
     e. Branch Specifier (blank for 'any') : main
     
     
     

3. **Jenkins** -> Choose the job that you just made -> Build Now.      #Run Tsunami scan 




# Description of the files in the REPO

1. **Jenkinsfile** - Runs the scan & Used to add / remove servers from list.

2. **Dockerfile**, **docker-compose.yml**, **flaskdtime.py** - Used separately, and not as part of the Pipeline. Their purpose is to run a container in a separate EC2 (which we are scanning - already installed on 3.127.66.246).

3. **shortreport.py** - Script for printing a short scan report.
     
     
     
# Servers for scanning:

1. 127.0.0.1 - The local server on which TSUNAMI is located.

*This is the only server that will warn about vulnerabilities (because unauthenticated Jupyter Notebook is also installed on it)

2. 77.125.40.74 - Random ip

3. 77.137.66.24 - Random ip

4. 3.127.66.246 - Aws ec2 with2 containers are already installed (from docker-compose.yml) 

* You can easily add or remove servers for scanning (Jenkinsfile, list) 
     ```
        stage('Create List') {
            steps {
                script {
                    list = ["127.0.0.1" , "77.125.40.74" , "77.137.66.24", "3.127.66.246"]
     ```
