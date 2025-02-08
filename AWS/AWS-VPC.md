**AWS VPC (Virtual Private Cloud) and Its Components**
======================================================

**What is AWS VPC?**
--------------------

Amazon **Virtual Private Cloud (VPC)** is a logically isolated network in AWS where you can deploy and manage AWS resources securely. It gives full control over networking, including **IP addressing, subnets, route tables, security groups, NAT, VPN, and peering**.

* * * * *

**AWS VPC Components**
----------------------

| **Component** | **Description** | **Key Considerations** |
| --- | --- | --- |
| **VPC** | A logically isolated network in AWS | Define IP range (CIDR block) |
| **Subnets** | A smaller network inside a VPC | Public or private subnets |
| **Route Tables** | Direct traffic within a VPC | Defines how traffic flows between subnets & internet |
| **Internet Gateway (IGW)** | Connects VPC to the internet | Required for public subnets |
| **NAT Gateway/NAT Instance** | Allows private subnets to access the internet | NAT Gateway is **highly available** (better than NAT Instance) |
| **Security Groups (SGs)** | Firewall at the instance level | Controls **inbound & outbound** traffic |
| **Network ACLs (NACLs)** | Firewall at the subnet level | Stateless, applies to all instances in a subnet |
| **VPC Peering** | Connects two VPCs privately | Works across **same or different AWS accounts** |
| **Transit Gateway** | Connects multiple VPCs | Centralized routing hub for **many VPCs** |
| **VPN Gateway (VGW)** | Secure site-to-site connection to on-premises | IPSec-based encryption |
| **Direct Connect (DX)** | Dedicated network link to AWS | Lower latency than VPN |
| **Elastic Load Balancer (ELB)** | Distributes traffic to multiple instances | Supports **Application (ALB), Network (NLB), and Classic (CLB) Load Balancers** |
| **AWS PrivateLink** | Connects VPCs securely to AWS services | Avoids **internet exposure** for AWS API calls |

* * * * *

**Different AWS VPC Setups and Their Comparison**
-------------------------------------------------

| **VPC Setup** | **Best Use Case** | **Pros** | **Cons** |
| --- | --- | --- | --- |
| **Single VPC with Public & Private Subnets** | Small apps, basic networking | Simple, easy to manage | Limited scalability |
| **Multi-VPC Architecture (Hub-Spoke Model)** | Multiple applications per account | **Security isolation**, clear segmentation | More complex routing |
| **VPC Peering** | Private communication between VPCs | Secure, low latency | No transitive routing |
| **Transit Gateway** | Large-scale multi-VPC networks | Scalable, centralized control | Higher cost |
| **AWS PrivateLink** | Secure connection to AWS services | **No internet exposure**, enhanced security | Service-specific usage |
| **VPC with Direct Connect (DX)** | Hybrid cloud with on-prem data centers | **Low latency**, consistent bandwidth | Requires dedicated connection |

* * * * *

**When to Use Which AWS VPC Setup?**
------------------------------------

✅ **Use a Single VPC** → If you have a **simple architecture** with a **few services**.\
✅ **Use VPC Peering** → If you need **low-latency private communication** between VPCs.\
✅ **Use Transit Gateway** → If you need **centralized routing for multiple VPCs**.\
✅ **Use AWS PrivateLink** → If you want to **connect to AWS services privately**.\
✅ **Use Direct Connect (DX)** → If you need **fast, dedicated hybrid cloud networking**