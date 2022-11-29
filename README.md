# Tsunami
Tsunami is a general purpose network security scanner with an extensible plugin
system for detecting high severity vulnerabilities with high confidence.

# The purpose of the scanner in the organization
In our organization there are servers that we would like to know if there are any vulnerabilities them.
We have another server on which tsunami scanner is installed(aws, ec2).

# Operating Instructions
* Before you start running, you must contact me so that I can turn on the EC2 on which the tsunami is installed.
1. **Jenkins** -> Manage nodes and clouds -> New node -> "linux" (name):             ## Guide to adding a Node for SSH access to AWS

     a. name : linux
     
     b. Remote root directory : /home/ubuntu
     
     c. Labels : linux
     
     d. Usage : Only build jobs with label expressions matching this node
     
     e. Launch method : launch agents via ssh
     
     f. Host : *ask me Ask me directly after I turn on the server
     
     g. Credentials -> add -> Credentials -> kind : 'ssh username with private key' , ID&Description : 'ubunto', Private Key : *past the content from .pem that i sent         in a separate email  
     
     h. Tool Locations -> home : /usr/bin/git ##for work with git
     
2. 
 
   


     ```
     nmap >= 7.80
     ncrack >= 0.7
     ```
