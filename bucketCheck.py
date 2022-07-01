import boto3
from botocore.exceptions import ClientError


class s3BucketLIst:

    def __init__(self, id, secret):
        self.id = id
        self.secret = secret
    
    def getbucketList(self):
        s3_client = boto3.client('s3', aws_access_key_id=self.id, aws_secret_access_key=self.secret)
        response = s3_client.list_buckets()
        buckets = []
        for bucket in response["Buckets"]:
            buckets += {bucket["Name"]}
        print(f"This is the available Bucket we can review: {buckets}")

class s3BucketAccess(s3BucketLIst):

    # Checking your S3 Bucket
    def accessCheck(self, buckettoreview):
        self.buckettoreview = buckettoreview
        s3_client = boto3.client('s3', aws_access_key_id=self.id, aws_secret_access_key=self.secret)

        # get public access block configurations
        aclResponse = s3_client.get_public_access_block(Bucket=self.buckettoreview)
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
        
class s3Encryption(s3BucketLIst):

    def checkEncryption(self, bucketencryption):
        self.bucketencryption = bucketencryption
        self.buckettoreview = self.bucketencryption
        s3_client = boto3.client('s3', aws_access_key_id=self.id, aws_secret_access_key=self.secret)
        try:
            # Use Client to Check Encryption of Bucket
            encryption = s3_client.get_bucket_encryption(Bucket=self.bucketencryption)
            encryptionRules = encryption["ServerSideEncryptionConfiguration"]["Rules"]
            print(f"{self.bucketencryption} is ENCRYPTED!")
            print(f"here is Encryption Rules {encryptionRules}")
        except ClientError as e:
            if e.response["Error"]["Code"] == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"{self.bucketencryption} is NOT ENCRYPTED!")
                print(f"This is the Error in ClientError: {e}")
            else:
                print(f"Bucket: unexpected error {self.bucketencryption}")