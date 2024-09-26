# Step-by-Step Guide for Dockerizing a Simple Python Program

## 1. Create a Simple Python Program

Create a file named `app.py` with the following content:

```python
print("Hello World in Python!")
```

## 2. Create a Dockerfile

Create a file named `Dockerfile` in the same directory as `app.py` with the following content:

```dockerfile
# Use a specific version of Python slim as the base image
FROM python:3.12.6-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the app.py file to the working directory
COPY app.py .

# Add a maintainer label
LABEL maintainer="Sarmad Rafique"

# Specify the command to run the app.py file
CMD ["python", "app.py"]
```

## 3. Build the Docker Image

Open a terminal in the directory containing the `Dockerfile` and run:

```sh
docker build -t docker_python .
```

## 4. Run the Docker Container

Run the container in the foreground to see the output:

```sh
docker run --name test_docker_python docker_python
```

## 5. Test the Docker Container

If you prefer to run the container in detached mode and check the logs:

1. **Run the Container in Detached Mode**:

    ```sh
    docker run --name test_docker_python -d docker_python
    ```

2. **Check the Logs**:

    ```sh
    docker logs test_docker_python
    ```

## 6. Push the Docker Image to Docker Hub

1. **Login to Docker Hub**:

    ```sh
    docker login
    ```

2. **Tag the Docker Image**:
    Replace `your_dockerhub_username` with your actual Docker Hub username.

    ```sh
    docker tag docker_python sarmad426/docker_python:latest
    ```

3. **Push the Docker Image**:

    ```sh
    docker push sarmad426/docker_python:latest
    ```

### Summary of Commands

```sh
# Build the Docker image
docker build -t docker_python .

# Option 1: Run the container in the foreground
docker run --name test_docker_python docker_python

# Option 2: Run the container in detached mode and check logs
docker run --name test_docker_python -d docker_python
docker logs test_docker_python

# Login to Docker Hub
docker login

# Tag the Docker image
docker tag docker_python your_dockerhub_username/docker_python:latest

# Push the Docker image to Docker Hub
docker push your_dockerhub_username/docker_python:latest
```
