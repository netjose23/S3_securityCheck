callBucketCheck.py calls Classes within bucketCheck.py. 
Call each Class and passing credentials (Store in a variable)
Pass the variable through to your function to run. 
    .getbucketLIst() gives you a list of all the buckets your credentials have access to

    .accessCheck("testbucket") gives you configuration info of the Bucket you pass through to it. In this example we pass "testbucket"

    .checkEncryption("testbucket") gives you the Encryption configuration of the Bucket "testbucket"
