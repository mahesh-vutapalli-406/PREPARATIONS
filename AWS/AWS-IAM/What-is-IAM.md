# What is IAM ??

IAM - IAM (Identity and Access Management) is a framework of policies and technologies that ensures the right individuals and systems have the appropriate access to resources.

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can manage permissions that control which AWS resources users can access.

When you signed in for the first time(while creating account) you will be signed in as root user with highest previlage access to your account.

### Service availability

IAM, like many other AWS services, is eventually consistent. IAM achieves high availability by replicating data across multiple servers within Amazon's data centers around the world. If a request to change some data is successful, the change is committed and safely stored. However, the change must be replicated across IAM, which can take some time. Such changes include creating or updating users, groups, roles, or policies. We recommend that you do not include such IAM changes in the critical, high-availability code paths of your application. Instead, make IAM changes in a separate initialization or setup routine that you run less frequently. Also, be sure to verify that the changes have been propagated before production workflows depend on them. For more information, see Changes that I make are not always immediately visible.

### Pricing

AWS Identity and Access Management (IAM), AWS IAM Identity Center and AWS Security Token Service (AWS STS) are features of your AWS account offered at no additional charge. You are charged only when you access other AWS services using your IAM users or AWS STS temporary security credentials.

IAM Access Analyzer external access analysis is offered at no additional charge. However, you will incur charges for unused access analysis and customer policy checks. For a complete list of charges and prices for IAM Access Analyzer, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing).

For information about the pricing of other AWS products, see the [Amazon Web Services pricing page.](https://aws.amazon.com/pricing/)

## HOW IAM WORKS?

Please check this page https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html 