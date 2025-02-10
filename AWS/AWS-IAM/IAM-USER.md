# IAM USER

An **IAM User** in AWS is an entity that represents a person or application that interacts with AWS services. Each IAM user has a unique name within an AWS account and can have specific permissions assigned through **IAM policies**.

### 🔹 **Key Features of IAM Users:**

1.  **Authentication** -- IAM users can sign in to AWS using a username and password.
2.  **Access Keys** -- Users can have access keys (Access Key ID & Secret Access Key) for programmatic access (CLI, SDK).
3.  **Permissions** -- Users don't have any permissions by default; they need to be assigned policies.
4.  **Groups** -- Users can be part of **IAM groups** to inherit permissions.
5.  **MFA (Multi-Factor Authentication)** -- Users can be required to use an additional authentication method.

### 🔹 **When to Use IAM Users?**

-   For individual **developers, administrators, or employees** who need AWS access.
-   When you need to provide **long-term credentials** (though roles are recommended for security).
-   When managing access for different people within an AWS account.
  
Creating an **IAM User** in AWS can be done in multiple ways:

* * * * *

**1️⃣ AWS Management Console (GUI) -- Step by Step with Images**
---------------------------------------------------------------

### **Step 1: Open IAM Dashboard**

-   Sign in to AWS Console → Go to **IAM** → Click on **Users**.

🔗 [AWS IAM Console](https://console.aws.amazon.com/iamv2)

### **Step 2: Click "Add User"**

-   Click **"Add User"** button.

### **Step 3: Configure User Details**

-   **User name** → Enter the name (e.g., `dev-user`).
-   **Access Type**
    -   ✅ AWS Management Console Access (for human users).
    -   ✅ Programmatic Access (for CLI, SDK, and API).

### **Step 4: Set Permissions**

-   Choose **one of the following**:
    -   Attach existing policies (e.g., `AdministratorAccess`, `AmazonS3FullAccess`).
    -   Add user to an IAM group.
    -   Create a custom permission policy.

### **Step 5: Enable MFA (Optional, but Recommended)**

-   Enable **Multi-Factor Authentication (MFA)** for extra security.

### **Step 6: Review & Create the User**

-   Download credentials (`.csv` file) and store them securely.

📌 **IAM User Created!** ✅

* * * * *

**2️⃣ AWS CLI -- Create IAM User**
---------------------------------

You can use the AWS CLI to create an IAM user with programmatic access.

### **Step 1: Create an IAM User**

`aws iam create-user --user-name dev-user`

### **Step 2: Attach a Policy to the User**

`aws iam attach-user-policy --user-name dev-user --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess`

### **Step 3: Create Access Key for the User**

`aws iam create-access-key --user-name dev-user`

🔹 This command returns `AccessKeyId` and `SecretAccessKey`. Store them securely.

* * * * *

**3️⃣ Python (Boto3) -- Create IAM User**
----------------------------------------

You can use the **Boto3** library in Python to create an IAM user programmatically.

### **Install Boto3**

`pip install boto3`

### **Python Script to Create an IAM User**

```
import boto3

# Initialize IAM client
iam = boto3.client('iam')

# Create IAM user
user_name = "dev-user"
response = iam.create_user(UserName=user_name)
print(f"IAM User {user_name} created successfully!")

# Attach a policy
policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
print("Policy attached successfully!")

# Create access key
access_key = iam.create_access_key(UserName=user_name)
print("Access Key Created:", access_key['AccessKey']['AccessKeyId'])
```

🔹 **Ensure AWS credentials are configured** (`aws configure`).

* * * * *

**4️⃣ Terraform -- Create IAM User**
-----------------------------------

Terraform allows you to automate IAM user creation as **Infrastructure as Code (IaC)**.

### **Step 1: Create Terraform File (`iam-user.tf`)**


```
provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_user" "dev_user" {
  name = "dev-user"
}

resource "aws_iam_user_policy_attachment" "attach_policy" {
  user       = aws_iam_user.dev_user.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

resource "aws_iam_access_key" "dev_user_key" {
  user = aws_iam_user.dev_user.name
}

output "access_key" {
  value     = aws_iam_access_key.dev_user_key.id
  sensitive = true
}

output "secret_key" {
  value     = aws_iam_access_key.dev_user_key.secret
  sensitive = true
}
```

### **Step 2: Run Terraform Commands**

```
terraform init
terraform apply -auto-approve
```

🔹 This will create an IAM user with access keys and attach the **AmazonS3FullAccess** policy.

* * * * *

**🎯 Summary -- Ways to Create IAM User**
----------------------------------------

| Method | Pros | Commands/Steps |
| --- | --- | --- |
| **AWS Console** | Easy to use, UI-based | IAM Console → Users → Add User |
| **AWS CLI** | Fast, scriptable | `aws iam create-user` |
| **Python (Boto3)** | Automates user creation in code | `iam.create_user()` |
| **Terraform** | Best for Infrastructure as Code (IaC) | `terraform apply` |