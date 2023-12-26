#!/bin/bash

# Prior to executing this script:
# 1. Attach the IAM Role 'S3-Admin-Access' to the Ubuntu EC2 instance
# 2. Update and upgrade the operating system
# 3. Install the AWS CLI: sudo apt install -y awscli
# 4. Reboot the EC2 instance from the AWS Console
# 5. From the EC2 instance download this script: aws s3 cp s3://gelc/setup.sh .

venv () {
    sudo apt install -y python3-pip
    sudo apt install -y python3-venv
    python3 -m venv my_env
    source "$HOME"/my_env/bin/activate
}

clear

venv

cd "$HOME"/my_env || { printf "cd failed, exiting\n" >&2; return 1; }
git clone https://github.com/laelgelc/gelc.git # Update the git repository link accordingly
cd "$HOME"/my_env/gelc || { printf "cd failed, exiting\n" >&2; return 1; }
pip install -r env.req # Make sure the file 'env.req' contains the requirements of the environment
aws s3 cp s3://gelc/.env .env # Update the reference to the '.env' file accordingly
