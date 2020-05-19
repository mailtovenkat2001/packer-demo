
import boto3

# Create IAM client
iam =boto3.client('iam',aws_access_key_id="AKIASAXBLKACHTCP4Z4K",aws_secret_access_key="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")

# Create user
response = iam.create_user(
    UserName='venkat-test'
)

print(response)
