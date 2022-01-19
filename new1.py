import boto3


def upload_file_to_bucket(file_name):
    BUCKET_NAME = 's3-myboard305files'
    S3_KEY = 'images/' + file_name
    s3 = boto3.client('s3')
    s3.upload_file(file_name, BUCKET_NAME, S3_KEY)

file_name='1.jpg'
upload_file_to_bucket(file_name)