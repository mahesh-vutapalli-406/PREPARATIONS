# IAM ROLE

An **IAM Role** in AWS is an identity that has **permissions to perform actions** on AWS services but **does not have long-term credentials** like a user. Instead, it provides **temporary security credentials** through AWS **STS (Security Token Service)**.

* * * * *

**🔹 Key Differences: IAM User vs. IAM Role**
---------------------------------------------

| Feature | IAM User | IAM Role |
| --- | --- | --- |
| **Identity Type** | Represents a person or application | Represents a set of permissions |
| **Authentication** | Uses **long-term credentials** (password, access keys) | Uses **temporary credentials** (AWS STS) |
| **Use Case** | Individual users, employees, or applications | AWS services, cross-account access, temporary access |

* * * * *

**🔹 When to Use IAM Roles?**
-----------------------------

-   **AWS Services (EC2, Lambda, etc.)** → Attach an IAM role to allow a service to access AWS resources.
-   **Cross-Account Access** → Allow users from another AWS account to assume a role.
-   **Federated Access** → Provide temporary AWS access to users via **SSO, Active Directory, or external identity providers**.
-   **Temporary Access** → Grant **limited-time** access to AWS services instead of using permanent credentials.

* * * * *

**🔹 Types of IAM Roles**
-------------------------

1.  **Service Roles** → Used by AWS services (e.g., an EC2 instance accessing S3).
2.  **Cross-Account Roles** → Allows access between AWS accounts.
3.  **Federated Roles** → Used for SSO with external identity providers (Okta, Google, AD).
4.  **IAM Role for Applications** → Used by applications to access AWS resources securely.

* * * * *
**Trust Policy (Who Can Assume a Role?)**
-----------------------------------------

A **Trust Policy** is used in **IAM Roles** to define **who (which AWS accounts, services, or users) is allowed to assume the role**. It is attached to an IAM **Role**, and it specifies who can **"assume"** or use the role via AWS **STS (Security Token Service)**.

### **🔹 Key Features of Trust Policy:**

✔️ Defines **who** can assume the role.\
✔️ Used **only with IAM Roles**.\
✔️ Always includes `"Action": "sts:AssumeRole"`.

* * * * *

### **Example of a Trust Policy (for EC2 Role)**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

📌 **Explanation:**

-   The **Principal** (`"Service": "ec2.amazonaws.com"`) allows AWS EC2 instances to assume this role.
-   The **Action** is `"sts:AssumeRole"`, which is required for roles.

* * * * *

**Resource Policy (Who Can Access a Resource?)**
------------------------------------------------------

A **Resource Policy** is attached to an **AWS resource** (such as **S3, KMS, SNS, SQS**) and defines **who can perform what actions on that resource**.

### **🔹 Key Features of Resource Policy:**

✔️ Defines **who can access a resource** and **what actions** they can perform.\
✔️ Used in **S3 Buckets, KMS, SNS, SQS, Secrets Manager**, etc.\
✔️ Can **allow cross-account access** without assuming a role.

* * * * *

### **Example of a Resource Policy (for S3 Bucket)**


```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:user/dev-user"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

📌 **Explanation:**

-   The **Principal** (`"AWS": "arn:aws:iam::111122223333:user/dev-user"`) allows a specific IAM user to access the S3 bucket.
-   The **Action** is `"s3:GetObject"`, meaning the user can **read objects** in the bucket.
-   The **Resource** is `"arn:aws:s3:::my-bucket/*"`, which refers to all objects in the bucket.

* * * * *

**🔹 Key Differences Between Trust Policy and Resource Policy**
---------------------------------------------------------------

| Feature | **Trust Policy** | **Resource Policy** |
| --- | --- | --- |
| **Purpose** | Controls **who can assume a role** | Controls **who can access a resource** |
| **Attached To** | IAM **Roles** | AWS **Resources** (S3, KMS, SQS, SNS, etc.) |
| **Defines** | **Who** can assume the role | **Who** can access a resource and **what** they can do |
| **Action Required** | Always includes `"sts:AssumeRole"` | Varies by service (e.g., `"s3:GetObject"`, `"kms:Decrypt"`) |
| **Cross-Account Access** | Needed for cross-account role assumption | Allows direct access to resources across accounts |

* * * * *

**🔹 When to Use Trust Policy vs. Resource Policy?**
----------------------------------------------------

| Use Case | Policy to Use |
| --- | --- |
| Allow **EC2 to assume an IAM Role** | **Trust Policy** |
| Allow **an IAM user to assume a role** | **Trust Policy** |
| Allow **cross-account role assumption** | **Trust Policy** |
| Allow **a different AWS account to access S3** | **Resource Policy** |
| Allow **a Lambda function to use a KMS key** | **Resource Policy** |
| Allow **SNS topic to send messages to an SQS queue** | **Resource Policy** |

* * * * *

**🔹 Example: IAM Role in Different Ways**
------------------------------------------

### **1️⃣ AWS Console (GUI)**

1.  Open **AWS IAM Console** → Go to **Roles** → Click **"Create Role"**.
2.  **Select trusted entity**:
    -   **AWS service** (e.g., EC2, Lambda).
    -   **Another AWS account** (for cross-account access).
    -   **Web Identity** (SSO, OpenID, Cognito).
3.  **Attach permissions policies** (e.g., `AmazonS3FullAccess`).
4.  **Name the role** and **create it**.
5.  **Attach the role** to a service (e.g., EC2).

* * * * *

### **2️⃣ AWS CLI -- Create an IAM Role**

#### **Step 1: Create a Trust Policy**

```
cat > trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Principal": { "Service": "ec2.amazonaws.com" },
    "Action": "sts:AssumeRole"
  }
}
EOF
```

#### **Step 2: Create the IAM Role**

`aws iam create-role --role-name MyEC2Role --assume-role-policy-document file://trust-policy.json`

#### **Step 3: Attach a Policy to the Role**

`aws iam attach-role-policy --role-name MyEC2Role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess`

* * * * *

### **3️⃣ Python (Boto3) -- Create IAM Role**

```
import boto3

iam = boto3.client('iam')

# Trust Policy
trust_policy = {
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Principal": { "Service": "ec2.amazonaws.com" },
        "Action": "sts:AssumeRole"
    }
}

# Create IAM Role
role = iam.create_role(
    RoleName="MyEC2Role",
    AssumeRolePolicyDocument=str(trust_policy)
)

# Attach a Policy
iam.attach_role_policy(
    RoleName="MyEC2Role",
    PolicyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess"
)

print(f"IAM Role {role['Role']['RoleName']} created successfully!")
```

* * * * *

### **4️⃣ Terraform -- Create IAM Role**

```
provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_role" "my_role" {
  name = "MyEC2Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "ec2.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "attach_s3" {
  role       = aws_iam_role.my_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}
```


`terraform init`
`terraform apply -auto-approve`

* * * * *

**🎯 Summary**
--------------

| Method | Steps |
| --- | --- |
| **AWS Console** | IAM → Roles → Create Role |
| **AWS CLI** | `aws iam create-role` + `aws iam attach-role-policy` |
| **Python (Boto3)** | `iam.create_role()` + `iam.attach_role_policy()` |
| **Terraform** | `aws_iam_role` + `aws_iam_role_policy_attachment` |