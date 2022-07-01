from bucketCheck import checkBucket, getbucketList

# You will use your Python Connector IAM user and input the Key ID and Secret Access Key Below
getbucketList({"aws_access_key_id"}, {"aws_secret_access_key"})

"""
You will pass the same Key Information you used above and include the... 
Bucket Name you would like to check (within Quotes) - Testing Class Implementation
"""
checkBucket({"aws_access_key_id"}, {"aws_secret_access_key"},{"YOUR_BUCKET_NAME"})
