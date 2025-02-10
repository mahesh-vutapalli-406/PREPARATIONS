### **Default Environment Variables in Jenkins** 🌍🚀

Jenkins provides several **built-in environment variables** that can be used in **Pipelines, Shell scripts, and Freestyle Jobs**.

* * * * *

**1\. Common Jenkins Environment Variables**
--------------------------------------------

| Variable | Description |
| --- | --- |
| **`BUILD_NUMBER`** | Current build number (e.g., `15`) |
| **`BUILD_ID`** | Unique identifier for the build (`YYYY-MM-DD_HH-MM-SS`) |
| **`BUILD_URL`** | URL to the Jenkins build (e.g., `http://jenkins/job/myjob/15/`) |
| **`JOB_NAME`** | Name of the job (e.g., `myjob`) |
| **`JOB_URL`** | URL of the job (e.g., `http://jenkins/job/myjob/`) |
| **`WORKSPACE`** | Directory where Jenkins executes the job |
| **`NODE_NAME`** | Name of the Jenkins agent (or `master` if running on the controller) |
| **`JENKINS_URL`** | URL of the Jenkins instance |
| **`JENKINS_HOME`** | Home directory of Jenkins (`/var/lib/jenkins`) |
| **`EXECUTOR_NUMBER`** | Unique number of the executor running the job |
| **`GIT_COMMIT`** | Current Git commit hash |
| **`GIT_BRANCH`** | Current Git branch being built |
| **`GIT_URL`** | Repository URL |

* * * * *

**2\. Default Variables in Pipeline Jobs**
------------------------------------------

These variables are available in **Declarative & Scripted Pipelines**.

groovy

CopyEdit

`pipeline {
    agent any
    stages {
        stage('Print ENV Variables') {
            steps {
                sh 'echo "Job Name: $JOB_NAME"'
                sh 'echo "Build Number: $BUILD_NUMBER"'
                sh 'echo "Workspace: $WORKSPACE"'
                sh 'echo "Node Name: $NODE_NAME"'
            }
        }
    }
}`

* * * * *

**3\. Accessing Environment Variables in a Script**
---------------------------------------------------

In a **Shell Script (Freestyle Job)**:

sh

CopyEdit

`echo "Job Name: $JOB_NAME"
echo "Build Number: $BUILD_NUMBER"
echo "Git Branch: $GIT_BRANCH"`

In a **Groovy Script**:

groovy

CopyEdit

`println "Job Name: ${env.JOB_NAME}"
println "Build Number: ${env.BUILD_NUMBER}"
println "Git Branch: ${env.GIT_BRANCH}"`

* * * * *

**4\. Custom Environment Variables**
------------------------------------

You can define custom environment variables in a **Pipeline**:

groovy

CopyEdit

`pipeline {
    agent any
    environment {
        PROJECT_NAME = "MyApp"
        DEPLOY_ENV = "Production"
    }
    stages {
        stage('Show Variables') {
            steps {
                sh 'echo "Project Name: $PROJECT_NAME"'
                sh 'echo "Deploying to: $DEPLOY_ENV"'
            }
        }
    }
}`

* * * * *

**5\. Special Jenkins Variables**
---------------------------------

| Variable | Description |
| --- | --- |
| **`BRANCH_NAME`** | Branch name (Multi-Branch Pipeline) |
| **`CHANGE_ID`** | PR/MR ID (for GitHub, GitLab, Bitbucket) |
| **`CHANGE_AUTHOR`** | Author of the pull request |
| **`CHANGE_BRANCH`** | Target branch for a PR |

* * * * *

### **Summary**

✅ Jenkins provides built-in environment variables for **build details, job info, Git, and system settings**.\
✅ You can access these in **Pipeline scripts, Shell scripts, and Groovy scripts**.\
✅ You can define **custom environment variables** inside the pipeline for flexibility.