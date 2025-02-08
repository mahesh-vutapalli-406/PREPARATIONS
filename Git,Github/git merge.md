**Git Merge & Merging Strategies -- Complete Guide**
===================================================

Git **merge** is used to combine changes from different branches. There are multiple **merging strategies** based on how changes should be integrated.

* * * * *

**🔹 1. Git Merge Basics**
--------------------------

Merging combines the changes from one branch into another, typically into `main` or `develop`.

### ✅ **Basic Merge Workflow**

1️⃣ Switch to the branch where you want to merge changes:

sh

CopyEdit

`git checkout main`

2️⃣ Merge another branch into it:

sh

CopyEdit

`git merge feature-branch`

3️⃣ Push changes to remote:

sh

CopyEdit

`git push origin main`

* * * * *

**🔹 2. Git Merging Strategies**
--------------------------------

Git uses different **merge strategies** depending on the project workflow and conflict handling.

| **Merge Strategy** | **Description** | **Best Used When** |
| --- | --- | --- |
| **Fast-Forward Merge** | Moves the branch pointer forward (no new commit) | Linear history without divergence |
| **Recursive Merge (Default)** | Creates a new merge commit | Two branches have diverged |
| **Squash Merge** | Combines multiple commits into one | Keep history clean before merging |
| **Octopus Merge** | Merges multiple branches at once | Used in multi-branch merges |

* * * * *

**🔹 3. Fast-Forward Merge (Default for Linear History)**
---------------------------------------------------------

If the branch to be merged is ahead with no divergence, Git performs a **fast-forward merge** (no extra commit).

🔹 **Example:**

sh

CopyEdit

`git checkout main
git merge feature-branch`

👉 The `main` branch pointer moves forward without a new merge commit.

🔹 **Force a Merge Commit (Avoid Fast-Forward):**

sh

CopyEdit

`git merge --no-ff feature-branch`

👉 This keeps a **merge commit** even if fast-forward is possible.

* * * * *

**🔹 4. Recursive Merge (Default for Diverged Branches)**
---------------------------------------------------------

If two branches have diverged, Git creates a **merge commit** to unify them.

🔹 **Example:**

sh

CopyEdit

`git checkout main
git merge feature-branch`

👉 This creates a **new commit** to merge both histories.

* * * * *

**🔹 5. Squash Merge (One Clean Commit)**
-----------------------------------------

Instead of keeping multiple commits, **squash merge** combines them into a single commit.

🔹 **Example:**

sh

CopyEdit

`git checkout main
git merge --squash feature-branch
git commit -m "Merged feature-branch as one commit"`

👉 This keeps a **clean commit history**.

* * * * *

**🔹 6. Merge Conflicts & Resolution**
--------------------------------------

### ✅ **Handling Merge Conflicts Manually**

If there are conflicts, Git will pause the merge and mark the conflicting files.

1️⃣ Check the conflicting files:

sh

CopyEdit

`git status`

2️⃣ Open the file and **resolve conflicts** manually.

3️⃣ Add the resolved files:

sh

CopyEdit

`git add resolved-file.txt`

4️⃣ Complete the merge:

sh

CopyEdit

`git commit -m "Resolved merge conflict"`

👉 To **abort** a merge if things go wrong:

sh

CopyEdit

`git merge --abort`

* * * * *

**🚀 Conclusion**
-----------------

Git merging strategies depend on your workflow:

-   **Fast-Forward Merge** (for linear history).
-   **Recursive Merge** (for diverged branches).
-   **Squash Merge** (for a clean commit).
-   **Merge Conflicts** can be resolved manually.