Docker Cheat Sheet
==================

1\. Docker Basics
-----------------

### Install Docker

-   Download & Install: [Docker Official Site](https://docs.docker.com/get-docker/)
-   Verify Installation:

    ```
    docker --version

    ```

### Docker Workflow

1.  **Pull Image**: `docker pull <image>`
2.  **Run Container**: `docker run <image>`
3.  **List Containers**: `docker ps`
4.  **Stop/Remove Containers**: `docker stop/rm <container>`
5.  **Build & Push Images**

### Common Commands

-   `docker images` -- List images
-   `docker ps -a` -- List all containers
-   `docker rmi <image>` -- Remove image
-   `docker inspect <container>` -- Inspect container details

2\. Working with Containers
---------------------------

### Run a Container

-   Run interactively:

    ```
    docker run -it <image> /bin/bash

    ```

-   Run in detached mode:

    ```
    docker run -d <image>

    ```

### Manage Containers

-   Stop container: `docker stop <container>`
-   Restart container: `docker restart <container>`
-   Remove container: `docker rm <container>`
-   View logs: `docker logs <container>`
-   Execute command in running container:

    ```
    docker exec -it <container> <command>

    ```

3\. Working with Images
-----------------------

### Pull & List Images

-   Pull an image: `docker pull <image>`
-   List images: `docker images`

### Build & Push Images

-   Build from Dockerfile:

    ```
    docker build -t <image-name> .

    ```

-   Tag and push:

    ```
    docker tag <image> <repo>:<tag>
    docker push <repo>:<tag>

    ```

4\. Docker Networking
---------------------

### List Networks

-   Show networks: `docker network ls`

### Create & Connect to Network

-   Create network: `docker network create <name>`
-   Run container in network:

    ```
    docker run --network=<name> <image>

    ```

5\. Docker Volumes
------------------

### Create & Use Volumes

-   Create volume: `docker volume create <name>`
-   Mount volume:

    ```
    docker run -v <name>:/path/in/container <image>

    ```

6\. Docker Compose
------------------

### Install & Use

-   Install Docker Compose: `sudo apt install docker-compose`
-   Example `docker-compose.yml`:

    ```
    version: '3'
    services:
      app:
        image: nginx
        ports:
          - "80:80"

    ```

-   Start with Compose: `docker-compose up -d`
-   Stop services: `docker-compose down`

7\. Docker Swarm (Orchestration)
--------------------------------

### Initialize Swarm

-   `docker swarm init`
-   Add worker: `docker swarm join-token worker`
-   Deploy stack: `docker stack deploy -c docker-compose.yml <stack-name>`

8\. Debugging & Logs
--------------------

-   Check logs: `docker logs <container>`
-   Inspect issues: `docker inspect <container>`
-   Check processes: `docker top <container>`

This Docker cheat sheet covers the most commonly used commands and workflows.