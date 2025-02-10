# IAM POLICY 

An **IAM Policy** in AWS is a document that defines permissions for an AWS resource. Policies are attached to IAM users, groups, or roles to grant or deny access to AWS resources. Each policy consists of one or more permissions that describe what actions are allowed or denied on specified resources.

Policies can be:

-   **Managed Policies**: Predefined by AWS (e.g., `AdministratorAccess`, `ReadOnlyAccess`).
-   **Inline Policies**: Custom policies defined within a specific IAM user, group, or role.
-   **Customer Managed Policies**: Custom policies created by users and attached to IAM users, groups, or roles.

A policy typically includes the following components:

-   **Version**: Defines the version of the policy language.
-   **Statement**: Contains the permissions (e.g., which actions are allowed, on which resources, and under what conditions).

* * * * * 

### Basic Structure of IAM Policy 

The basic structure of an **IAM Policy** in AWS follows a JSON format, and it generally consists of the following main components:

1.  **Version**: Specifies the version of the policy language.
2.  **Statement**: Contains the actual permissions and rules. Each statement can contain:
    -   **Effect**: Defines whether the action is allowed or denied (`Allow` or `Deny`).
    -   **Action**: Specifies which actions are allowed or denied (e.g., `s3:ListBucket`, `ec2:StartInstances`).
    -   **Resource**: Identifies the AWS resources on which the actions are performed (e.g., `arn:aws:s3:::my-bucket`).
    -   **Condition** (Optional): Specifies conditions for when the policy is applied (e.g., restrict access based on IP, time, etc.).

* * * * *

### **Basic IAM Policy Structure Example**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::my-bucket"
    },
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

### **Explanation of the Components:**

-   **Version**: `2012-10-17` is the latest policy language version as of now. Always use this version unless you have specific requirements.

-   **Statement**: This is an array that can contain one or more permission statements.

    -   **Effect**: Defines whether the action is allowed (`Allow`) or denied (`Deny`).

        -   `Allow`: Grants permission.
        -   `Deny`: Explicitly denies permission, overriding other "Allow" policies if there is a conflict.
    -   **Action**: Specifies which actions are allowed or denied. It can be a single action (like `s3:ListBucket`) or a wildcard (like `s3:*` for all actions on S3).

    -   **Resource**: Specifies the Amazon Resource Name (ARN) for the resources to which the actions apply. In the case of S3, it would be the ARN of the bucket or objects within the bucket.

        -   Example: `"arn:aws:s3:::my-bucket"` (bucket-level permission)
        -   Example: `"arn:aws:s3:::my-bucket/*"` (object-level permission)
    -   **Condition** (Optional): Allows you to set rules for when the policy should be applied. For example, only allow access if the request comes from a specific IP address or only during a specific time range.

* * * * *

### **Example with Condition**

```{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::my-bucket",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        }
      }
    }
  ]
}
```

In this case, the policy allows the `s3:ListBucket` action only if the request comes from the IP range `203.0.113.0/24`.

* * * * *

### **Full IAM Policy Structure**

Here's a breakdown of the full JSON structure of a policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",                        // Action is allowed
      "Action": "ec2:StartInstances",           // Action to perform
      "Resource": "arn:aws:ec2:region:account-id:instance/instance-id",  // Resource affected
      "Condition": {                            // Optional condition
        "StringEquals": {
          "aws:RequestTag/Project": "MyProject"
        }
      }
    },
    {
      "Effect": "Deny",                         // Explicit deny (overrides Allow if conflict)
      "Action": "s3:DeleteObject",              // Action to perform
      "Resource": "arn:aws:s3:::my-bucket/*"    // Resource affected
    }
  ]
}
```

### **Key Points to Remember:**

-   **Version**: Always use `"2012-10-17"` for the latest version of IAM policy language.
-   **Effect**: Can either be `Allow` or `Deny`. If both `Allow` and `Deny` policies are applied, `Deny` takes precedence.
-   **Action**: The permissions that can be granted. You can specify one or more actions, or use wildcards (e.g., `s3:*`).
-   **Resource**: The ARN of the resource on which the action is being performed. You can target specific resources (like a specific S3 bucket) or use wildcards for broad access.
-   **Condition** (Optional): You can specify conditions that limit when the policy is effective (e.g., IP address, time of day).

* * * * *

### **How to Create an IAM Policy**

Below are the steps to create an IAM Policy using **Python (Boto3)**, **AWS CLI**, **Terraform**, and **AWS Console**.

* * * * *

### **1\. Using Python (Boto3)**

To create a custom IAM policy in AWS using Python, you can use the `create_policy` method from the Boto3 IAM client. Here's an example:

```
import boto3

# Create an IAM client
iam_client = boto3.client('iam')

# Define the policy document
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::my-bucket"
        },
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}

# Create a new policy
response = iam_client.create_policy(
    PolicyName='MyS3Policy',
    PolicyDocument=str(policy_document)
)

print(response)
```

In this example, the policy grants permissions to list the bucket and get objects from a specific S3 bucket.

* * * * *

### **2\. Using AWS CLI**

You can create an IAM policy using the AWS CLI with the `create-policy` command. Here's how to do it:

1.  Save the policy document to a file, e.g., `policy.json`.


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::my-bucket"
        },
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}
```

1.  Use the `aws iam create-policy` command to create the policy:


`aws iam create-policy --policy-name MyS3Policy --policy-document file://policy.json`

This will create a custom policy named `MyS3Policy` with the permissions defined in the `policy.json` file.

* * * * *

### **3\. Using Terraform**

To create an IAM policy using Terraform, you need to define the policy as a resource. Here's an example:

```
provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_policy" "my_s3_policy" {
  name        = "MyS3Policy"
  description = "A policy to access a specific S3 bucket"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "s3:ListBucket"
        Resource = "arn:aws:s3:::my-bucket"
      },
      {
        Effect   = "Allow"
        Action   = "s3:GetObject"
        Resource = "arn:aws:s3:::my-bucket/*"
      }
    ]
  })
}
```

To create the policy, run the following Terraform commands:

`terraform init`
`terraform apply`

This will create a custom IAM policy named `MyS3Policy` with the permissions defined in the Terraform configuration.

* * * * *

### **4\. Using AWS Console**

You can create an IAM policy in the AWS Management Console using the following steps:

1.  Go to the [IAM Console](https://console.aws.amazon.com/iam/).

2.  In the left navigation pane, click **Policies**.

3.  Click the **Create Policy** button.

4.  Choose either the **Visual Editor** or the **JSON** tab to define your policy.

    -   **Visual Editor**: Use the user-friendly interface to select the services, actions, and resources you want to grant permissions to.
    -   **JSON**: Paste the policy JSON directly.

    Example policy JSON for S3 access:

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::my-bucket"
            },
            {
                "Effect": "Allow",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::my-bucket/*"
            }
        ]
    }
    ```

5.  Click **Review Policy**.

6.  Provide a name for the policy (e.g., `MyS3Policy`).

7.  Click **Create Policy**.

* * * * *

### **Summary**

-   **Python (Boto3)**: Use `create_policy` method with a JSON-formatted policy document.
-   **CLI**: Use `aws iam create-policy` command with a policy document in a JSON file.
-   **Terraform**: Define an `aws_iam_policy` resource with the policy document encoded in JSON.
-   **Console**: Use the IAM Management Console to create a policy using either the Visual Editor or JSON tab.