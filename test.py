import boto3
iam = boto3.resource('iam',aws_access_key_id='AKIAVOJJABES6ZKLQAXN',aws_secret_access_key='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')

created_user = iam.create_user(
            UserName='jenkinstest432'
            )
print(created_user)
