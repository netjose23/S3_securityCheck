from urllib import response
import boto3
from botocore.exceptions import ClientError


# get a bucket LIst 
def getbucketList(id, secret):
    s3_client = boto3.client('s3', aws_access_key_id=id, aws_secret_access_key=secret)
    response = s3_client.list_buckets()
    buckets = []
    for bucket in response["Buckets"]:
        buckets += {bucket["Name"]}
    print(f"This is the available Buckets we can review: {buckets}")


# Begin Checking your S3 Bucket 
def checkBucket(id, secret, buckettoreview):
    s3_client = boto3.client('s3', aws_access_key_id=id, aws_secret_access_key=secret)

    # Get Public Access Block Configurations
    aclResponse = s3_client.get_public_access_block(Bucket=buckettoreview)
    publicPolicy = aclResponse['PublicAccessBlockConfiguration']['BlockPublicPolicy']
    publicACLs = aclResponse['PublicAccessBlockConfiguration']['BlockPublicAcls']
    
    # Print out Responses of ACL and Policy settings within PublicAccessBlockConfiguration
    print(f"For {buckettoreview} The Policy Response is: {publicPolicy}")
    print(f"For {buckettoreview} ACL response: {publicACLs}")
    ACLandPolicy = publicACLs and publicPolicy
    if ACLandPolicy != True:
        print(f"Bucket {buckettoreview} Policy block and ACLs are set to False so Bucket IS PUBLIC!\n")
    else:
        print(f"Bucket {buckettoreview} is NOT Public because Policy and ACL are used\n")

    # check Encryption
    try:
        # Use Client to Check Encryption of Bucket
        encryption = s3_client.get_bucket_encryption(Bucket=buckettoreview)
        encryptionRules = encryption["ServerSideEncryptionConfiguration"]["Rules"]
        print(f"{buckettoreview} is ENCRYPTED!")
        print(f"here is Encryption Rules {encryptionRules}")
    except ClientError as e:
        if e.response["Error"]["Code"] == 'ServerSideEncryptionConfigurationNotFoundError':
            print(f"{buckettoreview} is NOT ENCRYPTED!")
            print(f"This is the Error in ClientError: {e}")
        else:
            print(f"Bucket: unexpected error {buckettoreview}")