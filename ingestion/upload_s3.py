import boto3, os, pathlib
from dotenv import load_dotenv
load_dotenv()
s3, BUCKET = boto3.client("s3", region_name=os.getenv("AWS_REGION")), os.getenv("S3_BUCKET")

def main():
    for p in pathlib.Path("data/raw").rglob("*"):
        if p.is_file():
            key = str(p.relative_to("data")).replace("\\", "/")
            s3.upload_file(str(p), BUCKET, key); print("uploaded", key)

if __name__ == "__main__":
    main()