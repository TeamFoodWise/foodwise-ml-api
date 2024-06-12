# Dockerfile based on ./deploy-history/Dockerfile.api
# and https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi
# Start from the official Python base image.
FROM python:3.9

# Set the current working directory to /root
WORKDIR /root

# Copy the file with the requirements to the /root directory.
COPY ./requirements.txt /root/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --default-timeout=100 --no-cache-dir --upgrade -r /root/requirements.txt

# Copy the ./X directory inside the /root directory.
COPY ./src /root/src
COPY ./data /root/data

# Set the command to run script
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
