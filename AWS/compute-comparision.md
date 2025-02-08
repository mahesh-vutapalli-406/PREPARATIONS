### **AWS Compute Services Comparison Table**

| **Service** | **Use Case** | **Key Features** | **Cost Model** | **Best When...** |
| --- | --- | --- | --- | --- |
| **EC2 (Elastic Compute Cloud)** | Virtual Machines (VMs) | Customizable instances, various CPU/memory options, supports auto-scaling | **Pay-per-use:** Per second/minute (On-Demand, Reserved, Spot) | You need full control over OS, storage, and network settings |
| **Lambda** | Serverless, event-driven computing | No server management, auto-scales, integrates with AWS services | **Pay-per-use:** Based on execution time & memory | You need quick execution of short-running processes without managing servers |
| **ECS (Elastic Container Service)** | Docker container orchestration | Fully managed, integrates with Fargate for serverless containers | **EC2 Mode:** Pay for underlying instances **Fargate Mode:** Pay per vCPU and memory usage | You need to run Docker containers without managing Kubernetes |
| **EKS (Elastic Kubernetes Service)** | Managed Kubernetes | Fully managed, integrates with AWS networking, auto-scaling | **EC2 Mode:** Pay for EC2 nodes **Fargate Mode:** Pay per vCPU and memory usage | You want to run Kubernetes without managing the control plane |
| **Fargate** | Serverless container compute | No EC2 provisioning, automatic scaling | **Pay-per-use:** CPU & memory per second | You need a fully managed, scalable container solution |
| **Lightsail** | Simple cloud hosting | Pre-configured VMs, includes networking & databases | **Fixed monthly pricing** | You need a low-cost, simple VM for websites or small apps |
| **Batch** | Processing large workloads | Auto-scales across compute resources, supports EC2 & Fargate | **Pay-per-use:** Based on EC2 or Fargate resources used | You need to run large-scale batch jobs efficiently |
| **Outposts** | AWS infrastructure on-premises | Hybrid cloud, fully managed AWS hardware in your data center | **CapEx & OpEx:** Requires upfront purchase & per-instance fees | You need AWS cloud services in your on-premises environment |
| **WaveLength** | Compute near 5G networks | Low-latency for edge computing & 5G applications | **Pay-per-use:** Similar to EC2 pricing | You need ultra-low-latency applications near mobile users |
| **Local Zones** | Compute closer to end-users | Reduces latency by extending AWS regions to more locations | **Pay-per-use:** Similar to EC2 pricing | You need ultra-low-latency computing in specific geographic areas |
| **Nitro Enclaves** | Secure, isolated compute environments | Protects sensitive data, cryptographic processing | **No extra cost** (included with EC2) | You need highly secure processing for sensitive workloads |

* * * * *

### **Cost Comparison by Compute Type**

| **Compute Type** | **Pricing Model** | **Typical Cost (Estimated)** |
| --- | --- | --- |
| **EC2 (On-Demand)** | Per second/minute | **$0.01 - $10/hr** (varies by instance type) |
| **EC2 (Spot Instances)** | Bidding-based pricing | **70-90% cheaper** than On-Demand |
| **Lambda** | Per request & execution time | **$0.00001667 per GB-second** |
| **ECS (Fargate Mode)** | Per vCPU and memory | **$0.04048 per vCPU/hr, $0.004445 per GB/hr** |
| **EKS (Fargate Mode)** | Per vCPU and memory | **Similar to ECS pricing** |
| **Lightsail** | Fixed monthly | **$3.50 - $160/month** |
| **Batch (EC2 Mode)** | Per EC2 usage | **Similar to EC2 pricing** |
| **Outposts** | Upfront + instance usage | **Varies (custom pricing)** |

🔹 **EC2 Reserved Instances** can be up to **75% cheaper** than On-Demand pricing.\
🔹 **Lambda is cost-effective** for short-lived functions but can be expensive for long-running applications.\
🔹 **Spot Instances** are the cheapest for flexible workloads but can be interrupted.

* * * * *

### **When to Use Which AWS Compute Service?**

✅ **Use EC2** → When you need full control over a virtual server.\
✅ **Use Lambda** → When you want **serverless computing** for event-driven applications.\
✅ **Use ECS/EKS** → When you need **container orchestration** (ECS for AWS-native, EKS for Kubernetes).\
✅ **Use Fargate** → When you want to **run containers without managing EC2 instances**.\
✅ **Use Lightsail** → When you need **simple, low-cost VM hosting**.\
✅ **Use Batch** → When you have **large-scale batch jobs** that require parallel processing.\
✅ **Use Outposts** → When you need **AWS compute power in your on-premises data center**.\
✅ **Use Local Zones or WaveLength** → When you require **low-latency computing near users**.