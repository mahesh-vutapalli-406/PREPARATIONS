**Complete Guide to Linux Commands (Categorized)**
==================================================

Here's a categorized list of essential **Linux commands**, with explanations and usage examples.

* * * * *

**🔹 1. File & Directory Operations**
-------------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `ls` | List files and directories | `ls -lah` (detailed list) |
| `cd` | Change directory | `cd /home/user` |
| `pwd` | Show current directory | `pwd` |
| `mkdir` | Create a new directory | `mkdir new_folder` |
| `rmdir` | Remove empty directories | `rmdir old_folder` |
| `rm` | Remove files/directories | `rm -rf folder_name` |
| `cp` | Copy files and directories | `cp file1.txt file2.txt` |
| `mv` | Move or rename files | `mv old.txt new.txt` |
| `touch` | Create an empty file | `touch newfile.txt` |
| `find` | Search for files | `find /home -name "*.txt"` |
| `tree` | Show directory structure | `tree /home` |

* * * * *

**🔹 2. File Content Manipulation**
-----------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `cat` | Display file contents | `cat file.txt` |
| `tac` | Display file in reverse order | `tac file.txt` |
| `less` | View file content page-by-page | `less file.txt` |
| `head` | Show first 10 lines of a file | `head -n 5 file.txt` |
| `tail` | Show last 10 lines of a file | `tail -n 5 file.txt` |
| `cut` | Extract parts of a file | `cut -d ':' -f 1 /etc/passwd` |
| `awk` | Process and analyze text | `awk '{print $1}' file.txt` |
| `sed` | Stream editor for modifying text | `sed 's/old/new/g' file.txt` |

* * * * *

**🔹 3. String Search & Processing**
------------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `grep` | Search for text in files | `grep "error" logfile.txt` |
| `egrep` | Extended grep (supports regex) | `egrep "pattern1 |
| `fgrep` | Fast grep (no regex) | `fgrep "error" logfile.txt` |
| `sort` | Sort lines in a file | `sort names.txt` |
| `uniq` | Find unique lines in a file | `uniq sorted.txt` |
| `wc` | Count lines, words, characters | `wc -l file.txt` |
| `diff` | Compare two files line by line | `diff file1.txt file2.txt` |

* * * * *

**🔹 4. User Management**
-------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `whoami` | Show current user | `whoami` |
| `id` | Show user ID and group ID | `id username` |
| `who` | Show logged-in users | `who` |
| `users` | Show current users | `users` |
| `passwd` | Change user password | `passwd username` |
| `adduser` | Add a new user | `adduser newuser` |
| `deluser` | Delete a user | `deluser username` |
| `groupadd` | Add a new group | `groupadd devs` |
| `usermod` | Modify user account | `usermod -aG sudo username` |

* * * * *

**🔹 5. Process Management**
----------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `ps` | List active processes | `ps aux` |
| `top` | Show real-time system usage | `top` |
| `htop` | Interactive process monitor | `htop` |
| `kill` | Terminate a process | `kill PID` |
| `pkill` | Kill processes by name | `pkill firefox` |
| `nice` | Start a process with a priority | `nice -n 10 myscript.sh` |
| `renice` | Change priority of a running process | `renice 5 PID` |

* * * * *

**🔹 6. Disk & Storage Management**
-----------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `df` | Show disk usage | `df -h` |
| `du` | Show directory size | `du -sh /home/user` |
| `mount` | Mount a filesystem | `mount /dev/sdb1 /mnt` |
| `umount` | Unmount a filesystem | `umount /mnt` |
| `fsck` | Check and repair filesystem | `fsck /dev/sda1` |

* * * * *

**🔹 7. Networking & Connectivity**
-----------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `ping` | Check network connectivity | `ping google.com` |
| `curl` | Fetch a webpage | `curl https://example.com` |
| `wget` | Download a file | `wget http://example.com/file.zip` |
| `netstat` | Show network connections | `netstat -tulnp` |
| `ss` | Show socket statistics | `ss -tulnp` |
| `ip` | Show IP addresses | `ip addr show` |
| `ifconfig` | Show network interfaces | `ifconfig eth0` |
| `traceroute` | Trace packet route to a host | `traceroute google.com` |

* * * * *

**🔹 8. System Monitoring & Performance**
-----------------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `uptime` | Show system uptime | `uptime` |
| `free` | Show memory usage | `free -m` |
| `vmstat` | Show system performance | `vmstat 1` |
| `iostat` | Show CPU and disk usage | `iostat` |
| `sar` | Collect system performance data | `sar -u 5 10` |

* * * * *

**🔹 9. Archiving & Compression**
---------------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `tar` | Archive files | `tar -cvf archive.tar mydir` |
| `tar -xvf` | Extract an archive | `tar -xvf archive.tar` |
| `gzip` | Compress files | `gzip file.txt` |
| `gunzip` | Decompress a file | `gunzip file.txt.gz` |
| `zip` | Create a zip file | `zip archive.zip file.txt` |
| `unzip` | Extract a zip file | `unzip archive.zip` |

* * * * *

**🔹 10. Package Management**
-----------------------------

| **Command** | **Description** | **Example Usage** |
| --- | --- | --- |
| `apt` | Manage packages (Debian/Ubuntu) | `apt install package-name` |
| `yum` | Manage packages (CentOS/RHEL) | `yum install package-name` |
| `dnf` | Manage packages (Fedora) | `dnf install package-name` |
| `rpm` | Manage RPM packages | `rpm -ivh package.rpm` |