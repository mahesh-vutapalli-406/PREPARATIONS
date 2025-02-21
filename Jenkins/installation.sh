#!/bin/bash

sudo yum update

sudo echo "downloading Jenkins repo  "

sudo echo "*********************************************************************************"

sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

sudo echo "*********************************************************************************"

sudo echo "importing jenkins key"

sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

sudo echo "*********************************************************************************"

sudo yum upgrade

sudo echo "*********************************************************************************"
sudo echo "installing java 17"

sudo dnf install java-17-amazon-corretto -y

sudo echo "*********************************************************************************"

sudo echo "installing git"

sudo yum install git -y 

sudo echo "*********************************************************************************"

sudo echo "installing jenkins"

sudo yum install jenkins -y

sudo echo "*********************************************************************************"


sudo echo "starting jenkins"

sudo systemctl enable jenkins

sudo systemctl start Jenkins

sudo echo "*********************************************************************************"


