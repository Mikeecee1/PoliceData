import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from pathlib import Path

from requests import session

# Load environment variables from .env file
load_dotenv()

def upload_file(filepath):
    """
    Upload a file to the configured AWS S3 bucket.

    Args:
        filepath (str): Path to the file to upload.

    Returns:
        bool: True if upload succeeds, otherwise False.
    """

    load_dotenv()

    file_path = Path(filepath)

    if not file_path.exists():
        print(f"File not found: {filepath}")
        return False
    
    # Create a session using the AWS credentials from environment variables
    session = boto3.Session(
        profile_name=os.getenv("AWS_PROFILE"),
        region_name=os.getenv("AWS_REGION")
    )

    s3 = session.client("s3")

    bucket_name = os.getenv("S3_BUCKET")

    folder = os.getenv("S3_FOLDER", "").strip()

    if folder:
        object_key = f"{folder}/{file_path.name}"
    else:
        object_key = file_path.name

    try:

        s3.upload_file(
            str(file_path),
            bucket_name,
            object_key
        )

        return True

    except ClientError as err:

        print(f"S3 upload failed: {err}")

        return False
    

    

