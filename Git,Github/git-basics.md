**GIT & GITHUB -- COMPLETE GUIDE**
=================================

Git is a **distributed version control system (VCS)** that helps developers track changes in code, collaborate efficiently, and maintain project history. GitHub is a cloud-based platform for hosting Git repositories.

* * * * *

**🔹 Key Git Topics & Commands**
--------------------------------

| **Concept** | **Description** | **Key Commands** |
| --- | --- | --- |
| **1\. Git Installation** | Install Git on your system | `git --version`, `sudo apt install git` (Linux), `brew install git` (Mac) |
| **2\. Git Configuration** | Configure username and email | `git config --global user.name "Your Name"`, `git config --global user.email "you@example.com"` |
| **3\. Git Repository (Repo)** | Create a new Git project | `git init` (initialize repo), `git clone <URL>` (copy repo) |
| **4\. Staging Area** | Prepare files for commit | `git add <file>` (stage file), `git add .` (stage all changes) |
| **5\. Commit** | Save changes to repo | `git commit -m "Message"` |
| **6\. Git Log & History** | View commit history | `git log`, `git log --oneline` |
| **7\. Branching** | Work on multiple versions of a project | `git branch <branch_name>`, `git checkout <branch_name>` |
| **8\. Merging** | Combine branches | `git merge <branch_name>` |
| **9\. Rebase** | Move or modify commit history | `git rebase <branch_name>` |
| **10\. Squash Commits** | Combine multiple commits into one | `git rebase -i HEAD~3` |
| **11\. Reset** | Undo changes in repo | `git reset --soft <commit>`, `git reset --hard <commit>` |
| **12\. Revert** | Undo commits without deleting history | `git revert <commit_hash>` |
| **13\. Stash** | Save uncommitted changes temporarily | `git stash`, `git stash pop` |
| **14\. Remote Repositories** | Connect to GitHub or other remote repo | `git remote add origin <URL>`, `git push origin main` |
| **15\. Fetch & Pull** | Get latest changes from remote | `git fetch`, `git pull origin main` |
| **16\. Submodules** | Include external repositories | `git submodule add <repo_url>` |
| **17\. Tags** | Create version tags for releases | `git tag -a v1.0 -m "Version 1.0"`, `git push origin --tags` |
| **18\. Blame** | Find who last changed a line in a file | `git blame <file>` |
| **19\. Cherry-pick** | Apply a specific commit to a branch | `git cherry-pick <commit_hash>` |
| **20\. Diff & Show** | Compare changes | `git diff`, `git show <commit_hash>` |
| **21\. Hooks** | Automate actions on Git events | `.git/hooks/` (custom scripts) |

* * * * *

**📌 Git & GitHub Workflow**
----------------------------

1️⃣ **Initialize a Repo:**

sh

CopyEdit

`git init
git add .
git commit -m "Initial commit"`

2️⃣ **Connect to GitHub:**

sh

CopyEdit

`git remote add origin <repository_URL>
git push -u origin main`

3️⃣ **Work on a Branch:**

sh

CopyEdit

`git checkout -b feature-branch`

4️⃣ **Merge Changes:**

sh

CopyEdit

`git checkout main
git merge feature-branch
git push origin main`

5️⃣ **Undo Changes (Reset & Revert):**

sh

CopyEdit

`git reset --soft HEAD~1  # Undo last commit but keep changes
git revert HEAD  # Revert last commit`