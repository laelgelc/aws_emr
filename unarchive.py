from dotenv import load_dotenv
import boto3
import pandas as pd
import tarfile
import bz2
import os
import sys
import shutil
import datetime

load_dotenv()  # This line brings all environment variables from .env into os.environ

# Define the name of the CSV file containing the list of URIs
uri_list = 'unarchive_uri_list_test.csv'
#uri_list = 'unarchive_uri_list_2011.csv'
#uri_list = 'unarchive_uri_list_2012.csv'
#uri_list = 'unarchive_uri_list_2013.csv'
#uri_list = 'unarchive_uri_list_2014.csv'
#uri_list = 'unarchive_uri_list_2015.csv'
#uri_list = 'unarchive_uri_list_2016.csv'
#uri_list = 'unarchive_uri_list_2017.csv'
#uri_list = 'unarchive_uri_list_2018.csv'
#uri_list = 'unarchive_uri_list_2019.csv'
#uri_list = 'unarchive_uri_list_2020.csv'
#uri_list = 'unarchive_uri_list_2021.csv'
#uri_list = 'unarchive_uri_list_2022.csv'
#uri_list = 'unarchive_uri_list_2023.csv'

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
input_directory = 'unarchive_data_input'

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
output_directory = 'unarchive_data_output'

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

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(uri_list, header=0)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    tar_file_key = row['filename S3 URI']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, ': Downloading ' + tar_file_key)
    s3.download_file(source_bucket_name, tar_file_key, input_directory)


    # Get a list of files in the output directory
#    files_to_copy = sorted(glob.glob(input_directory + '/*'))
    
    # Copy the downloaded files to the S3 bucket using the aws s3 cp command
#    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    print(timestamp, ': Transferring to ', destination, ' and clearing ', input_directory)
#    for file in files_to_copy:
#        subprocess.run(['aws', 's3', 'cp', file, destination], bufsize=0)
#        subprocess.run(['rm', '-f', file], bufsize=0)
    
    # Print timestamp after each download
#    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    print(timestamp, ': Download completed.')




# Set up the S3 bucket and file paths
#tar_file_key = 'path/to/your/tar/file.tar'

# Fetch the .tar file from the source S3 bucket
#s3.download_file(source_bucket_name, tar_file_key, 'file.tar')

# Uncompress the .tar file
#with tarfile.open('file.tar', 'r') as tar:
#    tar.extractall()

# Iterate over the extracted files
#for root, dirs, files in os.walk('.'):
#    for file in files:
#        if file.endswith('.bz2'):
#            # Uncompress each .bz2 file
#            with bz2.open(os.path.join(root, file), 'rb') as bz_file:
#                uncompressed_data = bz_file.read()
#                # Process the uncompressed data (e.g., write to a new file, parse JSON, etc.)
#                # Your processing logic goes here
#                
#                # Get the relative path of the file within the directory tree
#                relative_path = os.path.relpath(os.path.join(root, file), '.')
#
#                # Upload the processed file to the destination S3 bucket with the same directory tree structure
#                destination_key = os.path.join(relative_path, file)
#                s3.put_object(Body=uncompressed_data, Bucket=destination_bucket_name, Key=destination_key)
