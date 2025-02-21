import boto3
import time
import json

session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
)

group_name = "ec2_viewer_boto3-1" # group name
policy_name = "ec2_viewer_boto3-1" # policy name
group_policy_json = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Describe*",
                "ec2:GetSecurityGroupsForVpc"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
} # group policy json

iam_object = session.client('iam')
sts = session.client('sts')
account_id = sts.get_caller_identity()["Account"]

# GROUP creation

try:
    group_response = iam_object.create_group(
        GroupName = group_name
    )
    print(group_response)
    #print(f"groupname: {group_response["GroupName"]}\n ARN: {group_response["Arn"]}")
except iam_object.exceptions.EntityAlreadyExistsException:
    print("Group already existed")
    group_response = iam_object.get_group(
        GroupName= group_name
    )
    print(f"groupname: {group_response["GroupName"]}\n ARN: {group_response["Arn"]}")
    
# Group policy creation

try:
    policy_creation = iam_object.create_policy(
        PolicyName= policy_name,
        #Path='string',
        PolicyDocument= json.dumps(group_policy_json),
        Description='policy created to view only ec2',
        Tags=[
            {
                'Key': 'Name',
                'Value': policy_name
            },
        ]
    )
except iam_object.exceptions.EntityAlreadyExistsException:
    print("policy already exitsed")
     
# policy attachment
policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"
try:
    policy_attachment = iam_object.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
except:
    print("policy attachement failed")
    
# USER creation
    