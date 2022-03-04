import boto3

def create_bucket(bucket_name):
    client = boto3.client("s3")
    client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)