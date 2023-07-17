import boto3;

# Create IAM client
iam = boto3.client('iam')

paginator = iam.get_paginator('list_users')
for users in paginator.paginate():
    print(users)
    data = users['Users']

#delete all users
for user in data:
    ExistUserName = user['UserName']
    print(ExistUserName)
    if ExistUserName != 'ec2user':
        #iam.detach_user_policy(UserName = ExistUserName, PolicyArn =  'arn:aws:iam::aws:policy/AmazonEC2FullAccess')
        iam.delete_user(UserName = ExistUserName)

newUser='omkar';

for i in range(0,10):
    if(ExistUserName != newUser+ str(i)):
        # Create user
        response = iam.create_user(
                UserName = newUser + str(i)
        )
        print('User new created'+ newUser + str(i))

        #attach user policy
        iam.attach_user_policy(
            UserName = newUser,
            PolicyArn =  'arn:aws:iam::aws:policy/AmazonEC2FullAccess'
        )

#delete specific user
#iam.delete_user(
 #   UserName = 'IAM_USER_NAME2'
  #  )

#s3 bucket creation
s3_bucket = boto3.client('s3')
s3_bucket.create_bucket(Bucket = 'my-s3bucket-fromp-ython')