Dockerfile Cheat Sheet
======================

1\. Dockerfile Basics
---------------------

### Create a Dockerfile

-   Create a `Dockerfile` in your project directory.
-   Example:

    ```
    FROM ubuntu:latest
    COPY . /app
    RUN apt-get update && apt-get install -y python3
    CMD ["python3", "app.py"]

    ```

### Build an Image

-   Build from Dockerfile:

    ```
    docker build -t my-image .

    ```

2\. Dockerfile Instructions
---------------------------

### FROM (Base Image)

-   Defines the base image for the container.

    ```
    FROM node:14

    ```

### WORKDIR (Set Working Directory)

-   Sets the working directory inside the container.

    ```
    WORKDIR /app

    ```

### COPY & ADD (Copy Files)

-   Copy files from host to container.

    ```
    COPY . /app

    ```

-   `ADD` supports automatic extraction of compressed files.

    ```
    ADD archive.tar.gz /app/

    ```

### RUN (Execute Commands)

-   Runs commands during image build.

    ```
    RUN apt-get update && apt-get install -y curl

    ```

### CMD vs ENTRYPOINT

-   `CMD` sets default command:

    ```
    CMD ["nginx", "-g", "daemon off;"]

    ```

-   `ENTRYPOINT` sets fixed command:

    ```
    ENTRYPOINT ["nginx", "-g"]

    ```

### ENV (Set Environment Variables)

-   Define environment variables.

    ```
    ENV APP_ENV=production

    ```

### ARG (Build-Time Variables)

-   Define variables available during build.

    ```
    ARG VERSION=1.0

    ```

-   Usage:

    ```
    RUN echo "Version: $VERSION"

    ```

### EXPOSE (Define Ports)

-   Informs Docker which ports the container listens on.

    ```
    EXPOSE 8080

    ```

### VOLUME (Mount Persistent Storage)

-   Defines mount points for external storage.

    ```
    VOLUME /data

    ```

### HEALTHCHECK (Monitor Container Health)

-   Defines a health check command.

    ```
    HEALTHCHECK --interval=30s CMD curl -f http://localhost || exit 1

    ```

3\. Multi-Stage Builds
----------------------

-   Optimize image size using multiple stages.

    ```
    FROM golang:1.17 AS builder
    WORKDIR /app
    COPY . .
    RUN go build -o myapp

    FROM alpine:latest
    COPY --from=builder /app/myapp /usr/local/bin/
    CMD ["myapp"]

    ```

4\. Best Practices
------------------

-   Use minimal base images (`alpine`, `distroless`).
-   Reduce image layers by combining commands.
-   Use `.dockerignore` to exclude unnecessary files.
-   Minimize `RUN` layers to reduce final image size.

This cheat sheet provides a quick reference for writing Dockerfiles efficiently.