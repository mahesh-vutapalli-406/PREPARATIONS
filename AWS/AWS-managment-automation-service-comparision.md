**What is AWS SSM (AWS Systems Manager)?**
------------------------------------------

AWS **Systems Manager (SSM)** is a **management service** that helps you **monitor, manage, and automate** AWS resources, including **EC2, on-prem servers, and other AWS services**. It provides **patching, automation, secure shell access, and parameter storage**.

### **Key Features of AWS SSM:**

✅ **SSM Session Manager** → Secure **SSH/RDP access** to EC2 without using Bastion Hosts.\
✅ **SSM Patch Manager** → Automates **OS updates and security patches**.\
✅ **SSM Parameter Store** → Securely **stores and retrieves secrets** (API keys, DB credentials).\
✅ **SSM State Manager** → **Automates configuration management** (e.g., applying policies to EC2).\
✅ **SSM Inventory** → Collects and **tracks software/hardware inventory** of instances.\
✅ **SSM Automation** → Runs **predefined automation workflows** (e.g., restart EC2 on failure).

* * * * *

**Comparison of AWS Management & Automation Services**
------------------------------------------------------

| **Service** | **Purpose** | **Best Use Case** | **Key Features** | **Serverless?** | **Pricing Model** |
| --- | --- | --- | --- | --- | --- |
| **AWS SSM (Systems Manager)** | **Manage & automate AWS resources** | Centralized management of EC2, hybrid cloud, patching, secrets management | SSM Session Manager, Patch Manager, Parameter Store, Automation, Inventory | ✅ Yes | **Free for core features**, but **charges for advanced parameters & automation executions** |
| **AWS Config** | **Track & audit AWS resource configurations** | Compliance tracking, configuration history, security audits | Configuration snapshots, compliance checks, rule-based evaluation | ✅ Yes | Pay per **configuration rule evaluations** |
| **AWS CloudTrail** | **Log API calls & user activity** | Security auditing, forensic analysis, compliance monitoring | Logs AWS API calls, tracks user activity | ✅ Yes | **Free for last 90 days**, extra charges for storage |
| **AWS CloudWatch** | **Monitor AWS resources & applications** | Log monitoring, alerts, performance tracking | Logs, Metrics, Alarms, Dashboards, Insights | ✅ Yes | Pay per **log ingestion, metrics storage, and API requests** |
| **AWS OpsWorks** | **Configuration management (Chef & Puppet)** | Automating infrastructure using Chef/Puppet | Deploys & manages **Chef/Puppet-based stacks** | ❌ No (runs on EC2) | Pay for **EC2 instances** |
| **AWS Trusted Advisor** | **Optimize AWS usage & security** | Cost optimization, security improvement, best practices | Cost savings, security recommendations, fault tolerance checks | ✅ Yes | **Free for basic checks**, **paid for full recommendations** |

* * * * *

**When to Use Each Service?**
-----------------------------

| **Use Case** | **Best AWS Service** |
| --- | --- |
| **Securely access EC2 without SSH Keys/Bastion Hosts** | ✅ **AWS SSM Session Manager** |
| **Automate patch management for EC2 and on-prem servers** | ✅ **AWS SSM Patch Manager** |
| **Store and retrieve secure secrets & parameters** | ✅ **AWS SSM Parameter Store** (or AWS Secrets Manager) |
| **Monitor AWS infrastructure, logs, and metrics** | ✅ **AWS CloudWatch** |
| **Audit AWS resource changes & compliance tracking** | ✅ **AWS Config** |
| **Track API calls & user activity for security** | ✅ **AWS CloudTrail** |
| **Automate infrastructure with Chef/Puppet** | ✅ **AWS OpsWorks** |
| **Get AWS cost & security recommendations** | ✅ **AWS Trusted Advisor** |