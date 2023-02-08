import boto3
import pathlib
import os

def upload_file_using_client():
    s3 = boto3.client('s3')
    s3.upload_file(
    Filename="sample_file.txt",
    Bucket=bucket,
    Key=key,
    )

upload_file_using_client()
    