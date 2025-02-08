**AWS Identity and Access Management (IAM) -- Overview & Best Practices**
========================================================================

AWS **Identity and Access Management (IAM)** is a security service that helps you control access to AWS resources. It enables **user authentication, authorization, and access management** through fine-grained policies.

* * * * *

**1️⃣ Key Components of AWS IAM**
---------------------------------

| **IAM Component** | **Description** | **Example Use Case** |
| --- | --- | --- |
| **IAM Users** | Individual accounts with permissions | Developer, Admin, Data Analyst |
| **IAM Groups** | Collection of users sharing permissions | `Developers`, `Admins`, `Support Team` |
| **IAM Roles** | Temporary permissions assigned to AWS services or users | **EC2 instance role**, **Lambda execution role** |
| **IAM Policies** | JSON-based permissions defining what actions/resources are allowed/denied | "Allow S3 full access" policy for an IAM role |
| **IAM Identity Center (AWS SSO)** | Centralized access for multiple AWS accounts and apps | Managing users across **multiple AWS accounts** |

✅ **IAM is a global service** (it is not region-specific).

* * * * *

**2️⃣ IAM vs. Other AWS Security Services**
-------------------------------------------

| **Security Service** | **Purpose** | **Best For** |
| --- | --- | --- |
| **IAM** | Identity & access control | Managing AWS users, roles, and permissions |
| **AWS Organizations** | Multi-account management | Centralized control of multiple AWS accounts |
| **AWS Cognito** | User authentication | Web & mobile app login (OAuth, SAML, etc.) |
| **AWS STS (Security Token Service)** | Temporary access tokens | Granting short-term access to AWS resources |
| **AWS KMS** | Encryption key management | Managing encryption keys & secrets |

* * * * *

**3️⃣ IAM Policy Structure -- JSON Example**
-------------------------------------------

IAM **policies** define **who** can access **which AWS services and actions**. Below is a **basic JSON IAM policy**:

json

CopyEdit

`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::my-bucket"
        },
        {
            "Effect": "Deny",
            "Action": "s3:DeleteObject",
            "Resource": "arn:aws:s3:::my-bucket/*"
        }
    ]
}`

### **Key Elements in an IAM Policy**

✅ **Effect** → `Allow` or `Deny` permissions\
✅ **Action** → AWS API actions (`s3:ListBucket`, `ec2:StartInstances`)\
✅ **Resource** → Specifies which AWS resources are affected\
✅ **Condition (Optional)** → Additional restrictions (e.g., IP range, MFA required)

* * * * *

**4️⃣ IAM Roles vs. IAM Users -- When to Use What?**
---------------------------------------------------

| **Scenario** | **Use IAM Users?** | **Use IAM Roles?** |
| --- | --- | --- |
| **Developer needs access to AWS CLI/Console** | ✅ Yes | ❌ No |
| **EC2 needs access to S3 without credentials** | ❌ No | ✅ Yes |
| **Lambda function requires DynamoDB access** | ❌ No | ✅ Yes |
| **Third-party app (e.g., GitHub) needs AWS access** | ❌ No | ✅ Yes |

🔹 **IAM Users** → Best for **humans** logging into AWS Console or CLI.\
🔹 **IAM Roles** → Best for **AWS services** (e.g., EC2, Lambda) or **third-party access**.

* * * * *

**5️⃣ AWS IAM Security Best Practices**
---------------------------------------

### **✅ 1. Use IAM Roles Instead of IAM Users**

🔹 Never embed **AWS credentials in your code**. Instead, **use IAM roles** to grant temporary access.

### **✅ 2. Implement Least Privilege Access**

🔹 Assign only **necessary permissions** using the **Principle of Least Privilege**.\
🔹 Example: If a user only needs to read S3, grant `s3:ListBucket` but deny `s3:DeleteObject`.

### **✅ 3. Enable Multi-Factor Authentication (MFA)**

🔹 Require MFA for **IAM users, root accounts, and privileged roles**.\
🔹 AWS supports **virtual MFA apps, security keys, and hardware MFA devices**.

### **✅ 4. Rotate and Manage Credentials Securely**

🔹 Use **IAM Access Analyzer** to monitor unused access keys.\
🔹 Regularly rotate credentials **for security best practices**.

### **✅ 5. Use AWS Organizations & Service Control Policies (SCPs)**

🔹 Use **AWS Organizations** to enforce security rules across multiple AWS accounts.\
🔹 Example: SCPs can **block users from creating public S3 buckets**.

### **✅ 6. Monitor IAM Activity with AWS CloudTrail**

🔹 Enable **CloudTrail logs** to track **who accessed what** in AWS.\
🔹 Example: Get alerts if an IAM user creates a new policy.

* * * * *

**6️⃣ IAM Advanced Features**
-----------------------------

| **Feature** | **Description** | **Best For** |
| --- | --- | --- |
| **IAM Access Analyzer** | Detects unused IAM permissions | Security audits |
| **IAM Conditions** | Restrict access based on IP, time, MFA, etc. | Fine-grained access control |
| **IAM Policy Simulator** | Test IAM policies before applying them | Troubleshooting IAM issues |
| **IAM PassRole** | Allows one IAM role to grant permissions to another | Delegated access (e.g., Lambda assuming an EC2 role) |

* * * * *

**7️⃣ AWS IAM Pricing**
-----------------------

🔹 **IAM is free** → You can create unlimited **users, groups, and roles**.\
🔹 You only pay for **other AWS services** that IAM users/roles access.

* * * * *

**8️⃣ Summary -- When to Use Which IAM Feature?**
------------------------------------------------

| **Requirement** | **Best IAM Feature** |
| --- | --- |
| **Allow EC2 to access S3 securely** | ✅ **IAM Role** |
| **Control permissions for a group of users** | ✅ **IAM Groups** |
| **Limit permissions based on conditions (e.g., IP, MFA)** | ✅ **IAM Policy with Conditions** |
| **Audit IAM permissions and detect unused access** | ✅ **IAM Access Analyzer** |
| **Secure multiple AWS accounts under one policy** | ✅ **AWS Organizations & SCPs** |