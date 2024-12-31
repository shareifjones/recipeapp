import boto3
from botocore.exceptions import NoCredentialsError

s3 = boto3.client('s3')

def upload_to_s3(file_name, bucket='recipe-app-media', object_name=None):
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")


# Example usage
upload_to_s3('media/recipes/chicken.jpg')

