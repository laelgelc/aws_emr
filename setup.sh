#!/bin/bash

# Prior to executing this script:
# 1. Attach the IAM Role 'S3-Admin-Access' to the Ubuntu EC2 instance
# 2. Update and upgrade the operating system
# 3. Install the AWS CLI: sudo apt install awscli
# 4. Reboot the EC2 instance from the AWS Console
# 5. From the EC2 instance download this script: aws s3 cp s3://gelc/setup.sh .

update () {
    sudo apt update
    sudo apt upgrade -y

}

venv () {
    sudo apt install -y python3-pip
    sudo apt install -y python3-venv
    sudo apt install -y awscli
    python3 -m venv my_env
    source /home/ubuntu/my_env/bin/activate
}

git () {
    cd /home/ubuntu/my_env
    git clone https://github.com/laelgelc/gelc.git # Update the git repository link accordingly
    cd /home/ubuntu/my_env/gelc
    pip install -r env.req # Make sure the file 'env.req' contains the requirements of the environment
    aws s3 cp s3://gelc/.env01 .env # Update the reference to the '.env' file accordingly
}

clear

#update
venv
git