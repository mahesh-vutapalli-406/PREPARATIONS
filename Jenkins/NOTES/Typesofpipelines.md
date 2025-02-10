### **Different Types of Jobs in Jenkins** 🚀

Jenkins provides various job types to **automate CI/CD workflows**. Here are the most commonly used ones:

* * * * *

**1\. Freestyle Project** (Basic Job)
-------------------------------------

✅ **Best For:** Simple build/test/deploy tasks\
✅ **Key Features:**

-   GUI-based configuration
-   Supports SCM (Git, SVN, etc.)
-   Can execute shell scripts, batch commands, or Windows PowerShell
-   Supports build triggers (polling, webhooks, timers)

🔹 **How to Create a Freestyle Job:**

1.  Go to **Jenkins Dashboard → New Item → Freestyle Project**
2.  Configure **Source Code Management (SCM)** (e.g., Git)
3.  Add **Build Steps** (Shell commands, Maven, Gradle, etc.)
4.  Configure **Post-build actions** (Deploy, Email notification, etc.)

🔹 **Example:**

-   Clone a GitHub repository
-   Run unit tests with `mvn test`
-   Deploy to a server

* * * * *

**2\. Pipeline Project** (Scripted or Declarative)
--------------------------------------------------

✅ **Best For:** Complex workflows with multiple stages\
✅ **Key Features:**

-   Defined using a **Jenkinsfile**
-   Supports **Declarative** and **Scripted** pipelines
-   Supports agent selection, parallel execution, and post-build actions

🔹 **Example Jenkinsfile (Declarative Pipeline)**

groovy

CopyEdit

`pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}`

🔹 **Example Jenkinsfile (Scripted Pipeline)**

groovy

CopyEdit

`node {
    stage('Build') {
        sh 'mvn clean install'
    }
    stage('Deploy') {
        sh './deploy.sh'
    }
}`

* * * * *

**3\. Multi-Branch Pipeline**
-----------------------------

✅ **Best For:** Automating CI/CD for multiple Git branches\
✅ **Key Features:**

-   Automatically detects new branches
-   Executes different Jenkinsfiles per branch
-   Ideal for **GitFlow, feature branches, and PRs**

🔹 **How to Create a Multi-Branch Pipeline:**

1.  Go to **Jenkins Dashboard → New Item → Multi-Branch Pipeline**
2.  Select **Source Code Management (GitHub, Bitbucket, GitLab, etc.)**
3.  Jenkins automatically finds branches containing a `Jenkinsfile`

🔹 **Example Use Case:**

-   `dev` branch → Deploys to staging
-   `main` branch → Deploys to production

* * * * *

**4\. Maven Project**
---------------------

✅ **Best For:** Java applications using Maven\
✅ **Key Features:**

-   Built-in support for **Maven goals (clean, package, install, deploy)**
-   Parses `pom.xml` automatically
-   Supports integration with **SonarQube, Nexus, Artifactory**

🔹 **How to Create a Maven Job:**

1.  Go to **Jenkins Dashboard → New Item → Maven Project**
2.  Configure **SCM (Git, SVN, etc.)**
3.  Add **Maven Goals** (e.g., `clean install`)
4.  Configure **Post-Build Actions** (Publish reports, Deploy artifacts, etc.)

🔹 **Example Maven Build Goal:**

sh

CopyEdit

`mvn clean install -DskipTests`

* * * * *

**5\. Multiconfiguration (Matrix) Job**
---------------------------------------

✅ **Best For:** Running builds across multiple OS, JDK versions, or environments\
✅ **Key Features:**

-   Supports **cross-platform testing** (Windows, Linux, macOS)
-   Runs builds in **parallel** with different parameters

🔹 **Example Use Case:**

-   Test an application on **JDK 8, 11, and 17**
-   Deploy on **Ubuntu and CentOS** servers

🔹 **How to Configure:**

1.  Go to **Jenkins Dashboard → New Item → Multiconfiguration Project**
2.  Define **Axes** (e.g., `JDK Version`, `OS`)
3.  Configure **Build Steps** and **Post-Build Actions**

* * * * *

**6\. GitHub Organization Job**
-------------------------------

✅ **Best For:** Managing **all repositories** within a GitHub org\
✅ **Key Features:**

-   Automatically discovers repositories with a `Jenkinsfile`
-   Supports **multi-branch pipeline** setup

🔹 **How to Configure:**

1.  Go to **New Item → GitHub Organization**
2.  Add **GitHub Access Token**
3.  Jenkins scans for repositories with a `Jenkinsfile`

* * * * *

**7\. Bitbucket Team/Project Job**
----------------------------------

✅ **Best For:** Managing Jenkins pipelines for all Bitbucket repositories\
✅ **Key Features:**

-   Auto-discovers Bitbucket repositories
-   Supports **Multi-Branch Pipelines**

🔹 **How to Configure:**

1.  Install **Bitbucket Branch Source Plugin**
2.  Go to **New Item → Bitbucket Team/Project**
3.  Provide **Bitbucket credentials**

* * * * *

**8\. Folder Job**
------------------

✅ **Best For:** Organizing multiple Jenkins jobs\
✅ **Key Features:**

-   Creates a hierarchical structure of jobs
-   Can include **Freestyle, Pipelines, Multi-Branch Pipelines**

🔹 **How to Create a Folder:**

1.  Go to **New Item → Folder**
2.  Add jobs inside the folder

* * * * *

**Comparison Table**
--------------------

| Job Type | Use Case | Key Feature |
| --- | --- | --- |
| **Freestyle** | Simple projects | GUI-based, basic scripting |
| **Pipeline** | Complex CI/CD workflows | Uses Jenkinsfile (Declarative/Scripted) |
| **Multi-Branch Pipeline** | Branch-based CI/CD | Auto-discovers branches |
| **Maven** | Java + Maven builds | Auto-parses `pom.xml` |
| **Multiconfiguration (Matrix)** | Parallel testing | Runs across OS/JDK versions |
| **GitHub Organization** | Manages all GitHub repos | Auto-discovers repositories |
| **Bitbucket Team/Project** | Manages Bitbucket repos | Supports Bitbucket pipelines |
| **Folder** | Organizing jobs | Groups jobs in folders |