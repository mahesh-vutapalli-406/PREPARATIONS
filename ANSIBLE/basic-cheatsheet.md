Ansible Cheat Sheet
===================

1\. What is Ansible?
--------------------

Ansible is an open-source automation tool for configuration management, application deployment, and task automation. It uses SSH to communicate with remote hosts and employs YAML-based playbooks for defining automation tasks.

2\. Ansible Architecture
------------------------

### Key Components:

-   **Control Node**: The system where Ansible is installed and executed.
-   **Managed Nodes**: Remote systems managed by Ansible.
-   **Inventory**: A file defining hosts and groups.
-   **Modules**: Predefined functions to execute tasks.
-   **Playbooks**: YAML files that define automation workflows.
-   **Roles**: A way to organize playbooks into reusable components.
-   **Plugins**: Extend Ansible functionality.

3\. Ansible Installation
------------------------

### Install Ansible on Linux:

```
sudo apt update && sudo apt install ansible -y   # Ubuntu/Debian
sudo yum install ansible -y                      # CentOS/RHEL

```

### Verify Installation:

```
ansible --version

```

4\. Ansible CLI Commands
------------------------

### Ad-hoc Commands:

```
ansible all -m ping                    # Check connectivity to all hosts
ansible webservers -m shell -a "uptime" # Run a shell command on webservers group
ansible all -m copy -a "src=file.txt dest=/tmp/" # Copy a file to remote hosts

```

### Inventory Management:

```
ansible-inventory --list  # Display inventory in JSON format
ansible-inventory --graph # Show inventory structure

```

### Playbook Execution:

```
ansible-playbook site.yml   # Run a playbook
ansible-playbook -i inventory.ini playbook.yml # Specify inventory file

```

### Debugging & Testing:

```
ansible-playbook playbook.yml --check  # Dry run
ansible-playbook playbook.yml -vvv     # Verbose output

```

5\. Ansible Playbook Structure
------------------------------

### Basic Playbook Example:

```
- name: Deploy Web Server
  hosts: webservers
  become: yes
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present

    - name: Start Apache Service
      service:
        name: apache2
        state: started

```

### Playbook Breakdown:

-   `name`: Describes the playbook.
-   `hosts`: Defines target machines.
-   `become`: Runs tasks as sudo/root.
-   `tasks`: List of operations to execute.

6\. Dynamic Data in Playbooks
-----------------------------

### Using Variables:

```
- name: Install Package
  hosts: all
  vars:
    package_name: nginx
  tasks:
    - name: Install the package
      apt:
        name: "{{ package_name }}"
        state: present

```

### Using Facts:

```
- name: Display Host Facts
  hosts: all
  tasks:
    - name: Show OS Type
      debug:
        msg: "The system is running {{ ansible_distribution }} {{ ansible_version.full }}"

```

### Using Jinja2 Templates:

```
- name: Deploy Config File
  hosts: all
  tasks:
    - name: Generate Configuration
      template:
        src: config.j2
        dest: /etc/app/config.conf

```

**config.j2 Template Example:**

```
server_name = {{ inventory_hostname }}
port = {{ server_port }}

```

7\. Ansible Roles (Reusability)
-------------------------------

### Create Role Structure:

```
ansible-galaxy init my_role

```

### Role Directory Structure:

```
my_role/
├── tasks/main.yml
├── handlers/main.yml
├── templates/
├── files/
├── vars/main.yml
├── defaults/main.yml
├── meta/main.yml

```

### Using a Role in Playbook:

```
- name: Deploy Web Server
  hosts: webservers
  roles:
    - my_role

```

8\. Best Practices
------------------

-   Use **roles** for modular and reusable code.
-   Store **secrets** in Ansible Vault.
-   Use **handlers** to restart services only when needed.
-   Follow **idempotency** (ensure tasks only make changes when required).

This cheat sheet provides a quick reference to essential Ansible concepts and commands.