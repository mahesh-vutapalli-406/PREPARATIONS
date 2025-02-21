import boto3
import time
import json

import boto3.session

session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    #aws_session_token=SESSION_TOKEN
)
iam= session.client('iam')
sts = session.client('sts')
accountid = sts.get_caller_identity()["Account"]
creationtime = time.localtime()
role_name="boto3-role-creation"


policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1739899258751",
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

trustpolicy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": f"arn:aws:iam::{accountid}:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

try:
    response = iam.create_role(
        #Path='string',
        RoleName= role_name,
        AssumeRolePolicyDocument= json.dumps(trustpolicy),
        Description='created using boto3',
        MaxSessionDuration=3600,
        #PermissionsBoundary='string',
        Tags=[
            {
                'Key': "Creationtime",
                'Value': f"{creationtime.tm_mday}-{creationtime.tm_mon}-{creationtime.tm_year}"
            },
        ]
    )
except iam.exceptions.EntityAlreadyExistsException:
    response = iam.get_role(
    RoleName=role_name
    )
    print("Already role exists, and role details")
    print(response)

# policy creation
policy_name = "boto-role-policy"
try:
    ploicy_creation_response = iam.create_policy(
        PolicyName=policy_name,
        #Path=json.dumps(policy),
        PolicyDocument=json.dumps(policy),
        Description='boto3 policy',
        Tags=[
            {
                'Key': 'Creationdate',
                'Value': f"{creationtime.tm_mday}-{creationtime.tm_mon}-{creationtime.tm_year}"
            },
            {
                'Key': 'name',
                'Value': "mahesh"
            }
        ]
    )
except iam.exceptions.EntityAlreadyExistsException:
    print("policy alreay exitsts")
