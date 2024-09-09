# cloud_storage.py
import boto3

class CloudStorage:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_name):
        self.s3.upload_file(file_name, self.bucket_name, file_name)
        print(f"{file_name} uploaded to {self.bucket_name}")
