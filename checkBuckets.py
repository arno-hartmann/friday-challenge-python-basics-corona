import boto3
# Retrieve the list of existing buckets

def checkforBuckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print(response)
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

    if not response['Buckets']:
        return False
    else:
        return True