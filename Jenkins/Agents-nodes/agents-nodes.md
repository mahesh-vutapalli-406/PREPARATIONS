# Agents and Nodes in Jenkins (In Detail)

Understanding **Agents** and **Nodes** in Jenkins is crucial for mastering Jenkins architecture and distributed builds. Let's break this down in detail:

* * * * *

🌐 1. What are Nodes in Jenkins?
--------------------------------

A **Node** is any machine that is part of the Jenkins environment. It can be:

-   **Controller (Master Node)** -- The main Jenkins server.
-   **Agent (Slave Node)** -- Additional machines that offload build tasks from the Controller.

* * * * *

🖥️ 2. Controller (Previously called Master)
--------------------------------------------

The **Controller Node** is the central Jenkins instance responsible for:

-   Managing the Jenkins system configuration.
-   Storing job configurations and build history.
-   Distributing build tasks to Agents.
-   Handling the Jenkins UI and user requests.

🔑 Key Characteristics:

-   Can execute builds if no separate Agents are configured.
-   Usually **not recommended** to run heavy builds on Controller due to performance and stability concerns.

* * * * *

🛠️ 3. Agents (Previously called Slaves)
----------------------------------------

**Agents** are machines that perform the build, test, and deployment processes. They are launched by the Controller and can run Jenkins jobs.

🔑 Key Characteristics:

-   Perform the actual work (e.g., compiling code, running tests, deploying applications).
-   Help distribute workloads across multiple machines.
-   Can be physical machines, virtual machines, or containers.

* * * * *

🕸️ 4. Jenkins Distributed Build Architecture
---------------------------------------------

### Why Use Agents?

-   **Load Distribution:** Offloading work from the Controller.
-   **Parallel Execution:** Running multiple jobs simultaneously.
-   **Platform Diversity:** Different Agents can have different operating systems and software.
-   **Isolated Environments:** Agents can be configured to run specific types of builds.

* * * * *

🔗 5. Types of Agent Configurations
-----------------------------------

### (i) **Permanent Agent**

-   Manually configured via Jenkins UI.
-   Dedicated machine (or VM) permanently attached to the Controller.

### (ii) **Temporary (Dynamic) Agent**

-   Created on-demand (e.g., using Docker, Kubernetes, or cloud providers).
-   Auto-scaled based on workload.

### (iii) **Labels**

-   Tags assigned to nodes to control where a job runs.
-   Example: Label "linux" → Jobs requiring Linux build environment are run on nodes with this label.

* * * * *

⚙️ 6. Launch Methods (How Agents Connect to Controller)
-------------------------------------------------------

There are several ways for an Agent to communicate with the Controller:

### (i) **SSH**

-   Commonly used method.
-   The Controller connects to the Agent over SSH.

### (ii) **JNLP (Java Web Start)**

-   The Agent connects to the Controller.
-   Useful when the Agent is behind a firewall.

### (iii) **Windows Service**

-   Used to set up Agents on Windows machines.

### (iv) **Docker, Kubernetes, Cloud**

-   Dynamic Agents managed through cloud plugins.

* * * * *

🏗️ 7. How to Configure an Agent in Jenkins?
--------------------------------------------

### Step 1: Add a New Node

1.  Go to **Jenkins Dashboard** → **Manage Jenkins** → **Manage Nodes and Clouds** → **New Node**.
2.  Enter Node name, select **Permanent Agent**, and click OK.

### Step 2: Configure Node Details

-   **# of Executors:** Number of parallel builds the node can run.
-   **Remote Root Directory:** Directory on the Agent where Jenkins-related files will be stored.
-   **Labels:** Tags for job assignment.
-   **Launch Method:** SSH, JNLP, etc.

### Step 3: Launch the Agent

-   Based on the selected launch method, start the Agent.

* * * * *

📦 8. Key Terminology Recap
---------------------------

| Term | Description |
| --- | --- |
| **Node** | Any machine in the Jenkins environment. |
| **Controller (Master)** | Main Jenkins server, manages configurations and schedules builds. |
| **Agent (Slave)** | Machine that performs build tasks. |
| **Label** | Tags assigned to nodes to direct jobs to specific environments. |
| **Executor** | A slot on a node to execute a build. |

* * * * *

🧑‍💻 9. Practical Example
--------------------------

Suppose you have:

-   **Controller Node:** Manages Jenkins.
-   **Agent 1 (Linux):** Label -- `linux-build`
-   **Agent 2 (Windows):** Label -- `windows-build`

When you configure a job:

-   If the job requires Linux, assign the label `linux-build`.
-   Jenkins will schedule the job on **Agent 1**.

* * * * *

🚀 10. Best Practices
---------------------

-   Avoid running builds on the Controller.
-   Use **Labels** to assign jobs to appropriate environments.
-   Monitor Agent health regularly.
-   Use **Cloud Agents** (e.g., Kubernetes, AWS EC2) for auto-scaling.