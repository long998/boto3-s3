import boto3

'''download file from s3 bucket'''
s3 = boto3.resource('s3')
s3.Bucket('mybucket').download_file('hello.txt', '/tmp/hello.txt')

