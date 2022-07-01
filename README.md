# S3_securityCheck
 
Used callBucketCheck.py to input your Python Connector Credentials. Those credentials will pass to 
bucketCheck.py (Which holds the main code.) The first Function in callBucketCheck.py grabs the list of all your
S3_Buckets. The Second Function takes in your credentials again and takes your Bucket Name (that you received from the first function).
The checkBucket() function runs checks for Public Access and Encryption Status. The function presents the information in easy to read format. 