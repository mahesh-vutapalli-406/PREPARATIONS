**AWS Firewall Services -- Comparison & Use Cases**
==================================================

AWS provides multiple **firewall services** for different use cases, such as **network security, web application protection, and DDoS mitigation**. Below is a comparison of AWS firewall solutions, their **features, use cases, and when to use them**.

* * * * *

**1️⃣ AWS Firewall Services Overview**
--------------------------------------

| **Firewall Service** | **Best For** | **Layer** | **Traffic Type** | **DDoS Protection** | **Managed Rules** | **Integration** |
| --- | --- | --- | --- | --- | --- | --- |
| **AWS WAF (Web Application Firewall)** | Protects web applications from attacks like SQL injection, XSS | Layer 7 | HTTP/HTTPS | ✅ Yes (with AWS Shield) | ✅ Yes | ALB, API Gateway, CloudFront |
| **AWS Shield** | Protects against DDoS attacks | Layer 3 & 4 | Network & Web Traffic | ✅ Yes (Standard & Advanced) | ❌ No | ALB, NLB, CloudFront, Route 53 |
| **AWS Network Firewall** | Stateful firewall for **VPC-level** security | Layer 3 & 4 | VPC (TCP, UDP, ICMP) | ❌ No | ✅ Yes | VPC, Transit Gateway |
| **AWS Security Groups** | Instance-level firewall | Layer 4 | VPC (Inbound/Outbound) | ❌ No | ❌ No | EC2, RDS, Lambda, etc. |
| **AWS NACLs (Network Access Control Lists)** | Subnet-level firewall | Layer 3 | VPC (Inbound/Outbound) | ❌ No | ❌ No | VPC Subnets |

* * * * *

**2️⃣ AWS Firewall Services - When to Use Which?**
--------------------------------------------------

| **Use Case** | **Recommended AWS Firewall Service** |
| --- | --- |
| **Protect web apps from SQL injection, XSS, and bot attacks** | ✅ **AWS WAF** |
| **Mitigate DDoS attacks on web apps & network traffic** | ✅ **AWS Shield** |
| **Secure VPC traffic at the network level** | ✅ **AWS Network Firewall** |
| **Control inbound & outbound traffic for EC2 instances** | ✅ **Security Groups** |
| **Control traffic at the subnet level in a VPC** | ✅ **Network ACLs (NACLs)** |

* * * * *

**3️⃣ Deep Dive into Each AWS Firewall Service**
------------------------------------------------

### **🔹 AWS WAF (Web Application Firewall)**

✅ **Best For**: Protecting web applications against Layer 7 attacks (SQL injection, XSS, etc.).\
✅ **Works With**: **ALB, API Gateway, CloudFront**.\
✅ **Features**:

-   **Custom rule-based filtering**
-   **Managed rule groups** (AWS provides pre-configured rules)
-   **Rate-based throttling**
-   **Logging with CloudWatch**\
    ✅ **When to Use?** If you **host web applications** and need **protection against common web attacks**.

* * * * *

### **🔹 AWS Shield (DDoS Protection)**

✅ **Best For**: Protecting **websites, applications, and networks from DDoS attacks**.\
✅ **Works With**: **ALB, NLB, CloudFront, Route 53**.\
✅ **Features**:

-   **Shield Standard** (Free) → **Basic DDoS protection for AWS resources**.
-   **Shield Advanced** (Paid) → **24/7 attack monitoring, real-time response, and cost protection**.\
    ✅ **When to Use?** If your **application is vulnerable to DDoS attacks**, use **Shield Advanced** for enterprise-grade protection.

* * * * *

### **🔹 AWS Network Firewall**

✅ **Best For**: Protecting **VPCs from unauthorized access, malware, and packet-based threats**.\
✅ **Works With**: **VPC, AWS Transit Gateway**.\
✅ **Features**:

-   **Deep packet inspection (DPI)**
-   **Stateful filtering (track active connections)**
-   **Custom rule-based policies**
-   **Centralized firewalling for multiple VPCs**\
    ✅ **When to Use?** If you need **a centralized security solution for VPC traffic filtering and compliance**.

* * * * *

### **🔹 AWS Security Groups**

✅ **Best For**: Controlling **inbound and outbound** access for **EC2, RDS, Lambda, and other AWS services**.\
✅ **Works With**: **EC2, RDS, Lambda, Elastic Load Balancers, etc.**\
✅ **Features**:

-   **Instance-level firewall**
-   **Stateful traffic filtering**\
    ✅ **When to Use?** Always use **Security Groups** to **restrict access** to AWS resources.

* * * * *

### **🔹 AWS Network ACLs (NACLs)**

✅ **Best For**: Controlling **subnet-level** traffic in a **VPC**.\
✅ **Works With**: **VPC Subnets**.\
✅ **Features**:

-   **Stateless traffic filtering**
-   **Allow/Deny rules for inbound and outbound traffic**\
    ✅ **When to Use?** Use NACLs **when you need to filter traffic at the subnet level instead of the instance level**.

* * * * *

**4️⃣ AWS Firewall Services - Security Best Practices**
-------------------------------------------------------

### **✅ AWS WAF Best Practices**

-   Use **Managed Rule Groups** (pre-configured security rules).
-   Set up **rate-based rules** to mitigate bot traffic.
-   Log and analyze WAF data in **AWS CloudWatch**.

### **✅ AWS Shield Best Practices**

-   Enable **AWS Shield Advanced** for **real-time DDoS monitoring**.
-   Integrate with **AWS WAF** for **layered security**.

### **✅ AWS Network Firewall Best Practices**

-   Use **AWS Firewall Manager** to manage policies across multiple VPCs.
-   Integrate with **AWS GuardDuty** for **threat detection**.

### **✅ AWS Security Groups & NACLs Best Practices**

-   **Use least privilege** → Allow only required ports and IPs.
-   **Use NACLs for subnet-level protection** and **Security Groups for instance-level security**.
-   **Deny all traffic by default** and **explicitly allow required traffic**.

* * * * *

**5️⃣ AWS Firewall Services - Cost Comparison**
-----------------------------------------------

| **Service** | **Pricing Model** | **Estimated Cost** |
| --- | --- | --- |
| **AWS WAF** | Pay per rule per million requests | 💲💲 |
| **AWS Shield Standard** | Free | 💲 |
| **AWS Shield Advanced** | Flat fee + data processing charges | 💲💲💲 |
| **AWS Network Firewall** | Per firewall hour + per GB processed | 💲💲 |
| **Security Groups & NACLs** | Free (AWS charges for associated resources) | 💲 |

✅ **AWS Shield Standard is free** but **AWS WAF and Network Firewall incur costs based on traffic and rules**.\
✅ **AWS Shield Advanced is expensive** but provides **24/7 DDoS mitigation and financial protection**.

* * * * *

**6️⃣ Summary -- Which AWS Firewall to Choose?**
-----------------------------------------------

| **Requirement** | **Best Firewall Service** |
| --- | --- |
| **Protect web applications from SQL injection, XSS** | ✅ **AWS WAF** |
| **Mitigate large-scale DDoS attacks** | ✅ **AWS Shield Advanced** |
| **Secure VPC network traffic (stateful firewall)** | ✅ **AWS Network Firewall** |
| **Restrict traffic at the instance level (EC2, RDS, etc.)** | ✅ **Security Groups** |
| **Control traffic at the subnet level** | ✅ **Network ACLs (NACLs)** |
