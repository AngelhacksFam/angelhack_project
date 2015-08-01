import boto3

# Let's use Amazon s3

s3 = boto3.resource('s3')

# Just a test function
for bucket in s3.buckets.all():
	print(bucket.name)

# Look how simple uploading TXT files is to s3 bucket!
s3.Bucket('problem-upload').put_object(Key='test.txt', Body="Hello world!")

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName = 'test', Attributes = {'DelaySeconds': '5'})

# Access identifiers and Attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))

