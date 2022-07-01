from bucketCheck import s3BucketLIst, s3BucketAccess, s3Encryption

# You will use your Python Connector IAM user and input the Key ID and Secret Access Key Below
{variable} = s3BucketLIst({"aws_access_key_id"}, {"aws_secret_access_key"})
# Output in List format of all your Buckets your IAM user can access
{variableofAbove}.getbucketList()

# Check S3 Bucket Public Access Configuration - Creating boto3 client inerface
{Variable} = s3BucketAccess({"aws_access_key_id"}, {"aws_secret_access_key"})
# Get S3 Bucket of Choice Public Access Configuration
{variableofAbove}.accessCheck({"YOUR_BUCKET_NAME"})

# Check Encryption 
# Creating boto3 client interface
{Variable} = s3Encryption({"aws_access_key_id"}, {"aws_secret_access_key"})
# Check Encryption for the Bucket you are reviewing
{variableofAbove}.checkEncryption({"YOUR_BUCKET_NAME"})
