**AWS DevOps Services Comparison Table**
----------------------------------------

| **Service** | **Category** | **Best Use Case** | **Key Features** | **Pricing Model** | **Integration with AWS** | **Best When...** |
| --- | --- | --- | --- | --- | --- | --- |
| **CodeCommit** | **Source Control (Git Repository)** | Managed Git repositories | Secure, scalable Git hosting, integrates with CodePipeline | **Pay-per-use:** $1/user/month after 5 users | Deep integration with IAM, AWS Lambda, CodeBuild | You need a private Git repository with AWS integration |
| **CodeBuild** | **Continuous Integration (CI)** | Automated build & test pipelines | Fully managed build server, supports multiple languages | **Pay-per-use:** Based on compute usage (vCPU, memory) | Works with CodeCommit, GitHub, Bitbucket | You need serverless, scalable build environments |
| **CodePipeline** | **CI/CD Orchestration** | Automating CI/CD workflows | Manages multi-stage pipelines, integrates with multiple tools | **$1 per active pipeline/month** | Works with CodeCommit, S3, Lambda, ECS, EKS | You need an AWS-native CI/CD pipeline |
| **CodeDeploy** | **Deployment Automation** | Automated application deployments | Supports EC2, ECS, Lambda, and On-Prem | **Free for EC2/Lambda, $0.02 per on-prem instance** | Integrates with CloudFormation, Lambda, Auto Scaling | You need zero-downtime deployments |
| **CodeArtifact** | **Package Management** | Secure storage for dependencies | Supports Maven, npm, Python, Gradle | **Pay-per-use:** Based on storage & requests | Works with CodeBuild, CodePipeline | You need a managed package repository |
| **CodeStar** | **Project Management** | End-to-end DevOps management | Integrates all AWS DevOps tools | **Free** (Only pay for underlying services) | Provides pre-configured DevOps templates | You need a centralized DevOps management tool |
| **CloudFormation** | **Infrastructure as Code (IaC)** | Declarative AWS resource provisioning | Automates AWS infrastructure deployment | **Free** (Only pay for provisioned resources) | Works with AWS services like EC2, RDS, S3 | You need repeatable infrastructure deployment |
| **Terraform (3rd Party)** | **Infrastructure as Code (IaC)** | Multi-cloud infrastructure automation | AWS, Azure, GCP support, modular templates | **Free** (Enterprise plan available) | Works with AWS & non-AWS services | You need cross-cloud infrastructure management |
| **Elastic Beanstalk** | **PaaS Deployment** | Automatic infrastructure & application management | Supports Java, Python, Node.js, .NET, Ruby, etc. | **Free** (Only pay for underlying AWS services) | Manages EC2, Load Balancer, Auto Scaling | You want a **simple way to deploy web apps** |
| **OpsWorks** | **Configuration Management** | Automates infrastructure management | Chef/Puppet-based automation | **Free** (Pay for EC2, RDS, etc.) | Works with AWS and on-premises | You need **Chef/Puppet-based DevOps automation** |
| **AWS SAM (Serverless Application Model)** | **Serverless CI/CD** | Deploying serverless applications | Simplifies Lambda, API Gateway, DynamoDB deployment | **Free** (Only pay for AWS Lambda, API Gateway, etc.) | Works with CodePipeline, CloudFormation | You need an easy way to deploy **serverless apps** |

* * * * *

**Cost Comparison of AWS DevOps Services**
------------------------------------------

| **Service** | **Pricing Model** | **Typical Cost** |
| --- | --- | --- |
| **CodeCommit** | Free for first 5 users, then $1/user/month | **$1/user/month** |
| **CodeBuild** | Pay per vCPU & memory usage | **$0.005/min for small builds** |
| **CodePipeline** | $1 per active pipeline/month | **$1+/month** |
| **CodeDeploy** | Free for EC2/Lambda, $0.02 per on-prem instance | **Free - $0.02/instance** |
| **CodeArtifact** | Pay per storage & requests | **Starts at $0.05 per GB/month** |
| **CloudFormation** | Free (only pay for resources created) | **Free** |
| **Elastic Beanstalk** | Free (only pay for EC2, RDS, etc.) | **Depends on underlying AWS usage** |

* * * * *

**When to Use Which AWS DevOps Service?**
-----------------------------------------

✅ **Use CodeCommit** → When you need **private Git repositories** with AWS security.\
✅ **Use CodeBuild** → When you need **serverless build environments** for multiple languages.\
✅ **Use CodePipeline** → When you need **AWS-native CI/CD pipelines** with easy automation.\
✅ **Use CodeDeploy** → When you need **zero-downtime deployments** to EC2, ECS, Lambda.\
✅ **Use CodeArtifact** → When you need **secure dependency package management**.\
✅ **Use CloudFormation** → When you need **repeatable infrastructure provisioning**.\
✅ **Use Elastic Beanstalk** → When you want **easy PaaS deployment for web applications**.\
✅ **Use AWS SAM** → When you need **CI/CD for serverless applications**.\
✅ **Use Terraform** → When you need **multi-cloud Infrastructure as Code (IaC)**.