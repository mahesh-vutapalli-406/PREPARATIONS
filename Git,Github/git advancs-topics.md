**Git Advanced Topics -- Detailed Guide**
========================================

**🔹 1. Git Rebase**
--------------------

Git **rebase** moves a branch to a new base commit, making the commit history cleaner.

### ✅ **When to Use?**

-   To **rewrite history** and avoid unnecessary merge commits.
-   To **integrate changes** from one branch into another in a cleaner way.

### 🔹 **Key Rebase Commands & Usage**

sh

CopyEdit

`git checkout feature-branch
git rebase main`

👉 This applies commits from `feature-branch` on top of `main`.

🔹 **Interactive Rebase (Rewriting History):**

sh

CopyEdit

`git rebase -i HEAD~3`

👉 Allows modifying last 3 commits (squash, edit, reorder).

🔹 **Abort Rebase (If Conflicts Happen):**

sh

CopyEdit

`git rebase --abort`

🔹 **Continue After Resolving Conflicts:**

sh

CopyEdit

`git add .
git rebase --continue`

* * * * *

**🔹 2. Git Reset**
-------------------

Git **reset** is used to undo changes and move the HEAD pointer back to a previous state.

### ✅ **When to Use?**

-   To **undo commits** or **unstage changes**.
-   To **erase commit history** (caution with `--hard`).

### 🔹 **Key Reset Commands & Usage**

| Command | Effect |
| --- | --- |
| `git reset --soft HEAD~1` | Moves HEAD back by 1 commit but keeps changes staged |
| `git reset --mixed HEAD~1` | Moves HEAD back and unstages changes |
| `git reset --hard HEAD~1` | Moves HEAD back and deletes changes permanently |

* * * * *

**🔹 3. Git Squash**
--------------------

Git **squash** combines multiple commits into one, keeping history clean.

### ✅ **When to Use?**

-   To **combine related commits** before merging.
-   To **keep the commit history tidy**.

### 🔹 **Squash Commands**

1️⃣ Start interactive rebase for last 3 commits:

sh

CopyEdit

`git rebase -i HEAD~3`

2️⃣ Change `pick` to `squash` for commits you want to combine.

3️⃣ Save & exit, then **edit commit message** as needed.

* * * * *

**🔹 4. Git Submodules**
------------------------

Git **submodules** allow you to include other repositories inside your repository.

### ✅ **When to Use?**

-   To manage **external dependencies** in your project.
-   To include **shared libraries** across multiple projects.

### 🔹 **Submodule Commands & Usage**

1️⃣ **Add a submodule:**

sh

CopyEdit

`git submodule add <repo_url> path/to/submodule`

2️⃣ **Clone a repository with submodules:**

sh

CopyEdit

`git clone --recurse-submodules <repo_url>`

3️⃣ **Update all submodules:**

sh

CopyEdit

`git submodule update --init --recursive`

* * * * *

**🔹 5. Git Commit Messages & History**
---------------------------------------

### ✅ **Best Practices for Commit Messages**

-   Use **present tense** (`Add feature`, not `Added feature`).
-   Keep the **first line short** (50 chars max).
-   Provide **detailed context** if necessary in the description.

### 🔹 **View Commit History**

| Command | Effect |
| --- | --- |
| `git log` | Shows full commit history |
| `git log --oneline` | Shows a concise history |
| `git log --graph --oneline --all` | Visualize branches in commit history |
| `git show <commit_hash>` | Show changes for a specific commit |

* * * * *

**🔹 6. Git Blame (Find Who Changed What)**
-------------------------------------------

Git **blame** helps track who made changes to a file.

🔹 **Check Who Edited Each Line in a File:**

sh

CopyEdit

`git blame file.txt`