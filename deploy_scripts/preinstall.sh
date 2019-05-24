#!/bin/bash

cd /home/ec2-user
sudo yum -y update
sudo yum -y install python36
sudo yum -y install nginx
mkdir /home/ec2-user/pur-draft
