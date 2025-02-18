import boto3
import os

def upload_to_s3(file_name, bucket, object_name=None):
    """Uploads a file to an S3 bucket."""
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client.upload_file(file_name, bucket, object_name)
    print(f"Uploaded {file_name} to S3 bucket {bucket} as {object_name}")

if __name__ == "__main__":
    upload_to_s3("data/raw_data.csv", "your-s3-bucket-name")
