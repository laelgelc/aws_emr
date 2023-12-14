#!/bin/bash

# Prior to executing this script, attach the IAM Role S3-Admin-Access

clear

update () {
    sudo apt update
    sudo apt upgrade -y

}

venv () {
    sudo apt install python3-pip
    sudo apt install python3-venv
    sudo apt install awscli
    python3 -m venv my_env
    source /home/ubuntu/my_env/bin/activate
    pip install -r unarchive.req
}

