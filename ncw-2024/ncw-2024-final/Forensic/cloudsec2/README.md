# ある日、私が雲の中にいて攻撃されたとき
1. Find AWS credentials in website source code and use it to interact with API Gateway
2. Use API Gateway to interact with Lambda which list all Lambda functions
3. Use one of Lambda functions to get S3 bucket name 
4. Get AWS credentials from S3 bucket
5. Use AWS credentials to interact with S3 bucket and get the SSH private key
6. Use SSH private key to connect to the Droplet instance