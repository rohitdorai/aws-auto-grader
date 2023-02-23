import subprocess
import boto3
from botocore.exceptions import ClientError
import os
# Run the Python script
process = subprocess.Popen(['python', 'my_notebook.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Append a string to the output
processed_output = output.decode() + "\n\nProcessed by Docker!"

# Write the processed output to a file
with open('./output.txt', 'w') as f:
    f.write(processed_output)
    f.close()


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3', 
                      aws_access_key_id= 'AKIAUCLTZS76BWVWBB6I', 
                      aws_secret_access_key='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', 
                      region_name='us-east-1'
                      )
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file('./output.txt', 'autograderlambdatest')
print('Working')