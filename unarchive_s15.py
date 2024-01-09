# Edit the file '.env' and provide the required parameters
# Install the required libraries in the environment by executing: 'pip install -r env.req'

# Note about server sizing
# The server should have its disk space sized according to the following example:
#Unarchive instance 1: 30 GB + 240 GB = 270 GB
#- Largest archive to be extracted: 30 GB
#- Archive fully extracted: 8 * 30 GB = 240 GB
#
#Unarchive instances 2, 3 and 4: 3 GB + 24 GB = 27 GB (each)
#- Largest archive to be extracted: 3 GB
#- Archive fully extracted: 8 * 3 GB = 24 GB
#
#Server 1: 270 GB + 81 GB + 3 GB = 354 GB ~ 360 GB
#- Unarchive instances 1: 270 GB
#- Unarchive instances 2, 3 and 4: 3 * 27 GB = 81 GB
#- Operating system: 3 GB

# Importing the required libraries
from dotenv import load_dotenv
import boto3
import pandas as pd
import tarfile
import zipfile
import bz2
import os
import sys
import shutil
import datetime

load_dotenv()  # This line brings all environment variables from '.env' into 'os.environ'

# Define the name of the CSV file containing the list of S3 keys
key_list = os.environ['KEY_LIST']
#key_list = 'unarchive_key_list_test.csv'
#key_list = 'unarchive_key_list_2011.csv'
#key_list = 'unarchive_key_list_2012.csv'
#key_list = 'unarchive_key_list_2013.csv'
#key_list = 'unarchive_key_list_2014.csv'
#key_list = 'unarchive_key_list_2015.csv'
#key_list = 'unarchive_key_list_2016.csv'
#key_list = 'unarchive_key_list_2017.csv'
#key_list = 'unarchive_key_list_2018.csv'
#key_list = 'unarchive_key_list_2019.csv'
#key_list = 'unarchive_key_list_2020.csv'
#key_list = 'unarchive_key_list_2021.csv'
#key_list = 'unarchive_key_list_2022.csv'
#key_list = 'unarchive_key_list_2023.csv'

# Set up AWS credentials
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = os.environ['REGION_NAME']

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Set up the source and destination S3 bucket names
source_bucket_name = os.environ['SOURCE_BUCKET_NAME']
destination_bucket_name = os.environ['DESTINATION_BUCKET_NAME']

# Define the name of the directory where the downloaded files will be stored
input_directory = os.environ['INPUT_DIRECTORY']

# Check if the input directory already exists. If it does, remove it and its contents. If it doesn't exist, create it.
if os.path.exists(input_directory):
    shutil.rmtree(input_directory)
    print('Old output directory successfully removed.')
    try:
        os.makedirs(input_directory)
        print('Output directory successfully created.')
    except OSError as e:
        print('Failed to create the directory:', e)
        sys.exit(1)
else:
    try:
        os.makedirs(input_directory)
        print('Output directory successfully created.')
    except OSError as e:
        print('Failed to create the directory:', e)
        sys.exit(1)

# Define the name of the directory where the unarchived files will be stored
output_directory = os.environ['OUTPUT_DIRECTORY']

# Check if the output directory already exists. If it does, remove it and its contents. If it doesn't exist, create it.
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)
    print('Old output directory successfully removed.')
    try:
        os.makedirs(output_directory)
        print('Output directory successfully created.')
    except OSError as e:
        print('Failed to create the directory:', e)
        sys.exit(1)
else:
    try:
        os.makedirs(output_directory)
        print('Output directory successfully created.')
    except OSError as e:
        print('Failed to create the directory:', e)
        sys.exit(1)

# Read the key CSV file into a pandas DataFrame
df = pd.read_csv(key_list, header=0)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    file_key = row['filename-destination']
    input_file_path = input_directory + '/' + file_key
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, ': Downloading ' + file_key)
    s3.download_file(source_bucket_name, file_key, input_file_path)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, ': Extracting ' + file_key)
    if input_file_path.endswith('.tar') or input_file_path.endswith('.tar.gz'):
        with tarfile.open(input_file_path, 'r') as tar:
            tar.extractall(path=output_directory)
    elif input_file_path.endswith('.zip'):
        with zipfile.ZipFile(input_file_path, 'r') as zip:
            zip.extractall(path=output_directory)
    else:
        print(f'Error: {input_file_path} is not a supported archive file.')
    # Iterate over the extracted files
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, ': Extracting and transferring .bz2 files to S3 for ' + file_key)
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            if file.endswith('.bz2'):
                # Uncompress each .bz2 file
                with bz2.open(os.path.join(root, file), 'rb') as bz_file:
                    uncompressed_data = bz_file.read()
                    
                    # Remove the .bz2 extension from the filename
                    uncompressed_filename = file[:-4]
                    
                    # Get the relative path of the file within the directory tree
                    relative_path = os.path.relpath(os.path.join(root, file), '.')
                    
                    # Upload the processed file to the destination S3 bucket with the same directory tree structure
                    destination_key = os.path.join(relative_path, uncompressed_filename)
                    s3.put_object(Body=uncompressed_data, Bucket=destination_bucket_name, Key=destination_key)
                    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(timestamp, ':', uncompressed_filename, 'transferred')
    shutil.rmtree(input_directory)
    os.makedirs(input_directory)
    shutil.rmtree(output_directory)
    os.makedirs(output_directory)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, ': Input and output directories cleared out for ' + file_key)
