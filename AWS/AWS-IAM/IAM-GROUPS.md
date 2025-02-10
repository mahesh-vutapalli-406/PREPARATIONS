An **IAM Group** in AWS (Identity and Access Management) is a collection of IAM users that are grouped together for easier management of permissions. Rather than assigning permissions to each individual user, you can assign policies to the group, and any user added to the group inherits the group's permissions. This makes it more efficient when managing multiple users with similar roles.

### Creating an IAM Group

Here's how to create an IAM Group in AWS using **Python (Boto3)**, **AWS CLI**, **Terraform**, and **AWS Console**.

* * * * *

### 1\. **Using Python (Boto3)**

Boto3 is AWS's Python SDK, which allows you to interact with AWS services.

```
import boto3

# Create an IAM client
iam_client = boto3.client('iam')

# Create a new IAM group
response = iam_client.create_group(
    GroupName='MyNewGroup'
)

print(response)
```

This will create an IAM group named `MyNewGroup`. You can also add policies to the group after creating it.

* * * * *

### 2\. **Using AWS CLI**

You can use the AWS Command Line Interface (CLI) to create an IAM group by running the following command:

`aws iam create-group --group-name MyNewGroup`

To attach a policy to the group after creating it:

`aws iam attach-group-policy --group-name MyNewGroup --policy-arn arn:aws:iam::aws:policy/AdministratorAccess`

Replace `AdministratorAccess` with the policy you want to attach.

* * * * *

### 3\. **Using Terraform**

Here's how you can create an IAM group using **Terraform**:

1.  First, create a Terraform configuration file, `iam_group.tf`.

```
provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_group" "my_group" {
  name = "MyNewGroup"
}

resource "aws_iam_group_policy_attachment" "my_group_policy" {
  group      = aws_iam_group.my_group.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
```

1.  Then run the following Terraform commands:

`terraform init`
`terraform apply`

This will create the IAM group `MyNewGroup` and attach the `AdministratorAccess` policy to it.

* * * * *

### 4\. **Using AWS Management Console**

1.  Go to the [IAM Console](https://console.aws.amazon.com/iam/).
2.  In the left navigation pane, click **Groups**.
3.  Click **Create New Group**.
4.  Enter the name for your group (e.g., `MyNewGroup`).
5.  Choose the permissions policies you want to attach to the group.
6.  Click **Create Group**.

* * * * *

### Summary

-   **Python (Boto3)**: Use `create_group` method.
-   **CLI**: Use `aws iam create-group` command.
-   **Terraform**: Define an `aws_iam_group` resource.
-   **Console**: Navigate to IAM groups section and use the wizard.