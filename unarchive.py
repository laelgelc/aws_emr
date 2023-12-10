import boto3
import tarfile
import bz2
import os

# Set up AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Set up EMR client
emr = boto3.client('emr', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Set up the job flow
job_flow_id = 'YOUR_JOB_FLOW_ID'

# Set up the source and destination S3 bucket names
source_bucket_name = 'YOUR_SOURCE_BUCKET_NAME'
destination_bucket_name = 'YOUR_DESTINATION_BUCKET_NAME'

# Set up the S3 bucket and file paths
tar_file_key = 'path/to/your/tar/file.tar'

# Fetch the .tar file from the source S3 bucket
s3.download_file(source_bucket_name, tar_file_key, 'file.tar')

# Uncompress the .tar file
with tarfile.open('file.tar', 'r') as tar:
    tar.extractall()

# Iterate over the extracted files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.bz2'):
            # Uncompress each .bz2 file
            with bz2.open(os.path.join(root, file), 'rb') as bz_file:
                uncompressed_data = bz_file.read()
                # Process the uncompressed data (e.g., write to a new file, parse JSON, etc.)
                # Your processing logic goes here
                
                # Get the relative path of the file within the directory tree
                relative_path = os.path.relpath(os.path.join(root, file), '.')

                # Upload the processed file to the destination S3 bucket with the same directory tree structure
                destination_key = os.path.join(relative_path, file)
                s3.put_object(Body=uncompressed_data, Bucket=destination_bucket_name, Key=destination_key)

# Terminate the EMR cluster
emr.terminate_job_flows(JobFlowIds=[job_flow_id])
