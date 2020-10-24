import boto3

'''download file from s3 bucket'''
s3 = boto3.resource('s3')
s3.Bucket('mybucket').download_file('hello.txt', '/tmp/hello.txt')

#download object, using open file as object
bucket = s3.Bucket('meykey')
with open('filename', 'wb') as data:
    bucket.download_fileobj('mykey', data)

#clear using bucket to access file. but you can use client or resource.
s3 = boto3.resource('s3')
s3.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')

#upload
data = b'hello,it is add info'
bucket.upload_fileobj(data, 'mykey')

#same, you can use resource or client
s3.upload_fileobj(data, 'mybucket', 'mykey')

#the bucket exit by name
try:
    response = client.head_bucket(
        Bucket='bucketname'
    )
except NoSuchBucket:
    pass

#the bucket exit by key
try:
    response = client.head_object(
        Bucket='bucketname',
        Key = 'mykey'
    )
except NoSuchKey:
    pass

