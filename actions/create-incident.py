
import boto3

def start_ec2_instance():
    # Create an EC2 client
    ec2_client = boto3.client(
        'ec2',
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region
    )

    # Start the EC2 instance
    response = ec2_client.start_instances(
        InstanceIds=[instance_id]
    )

    return response

# Read parameters from StackStorm context
instance_id = '{{}}'
access_key_id = '{{}}'
secret_access_key = '{{}}'
region = 'us-east-1'  # Update with your specific region

# Start the EC2 instance
response = start_ec2_instance()

print(response)
