#!/bin/sh

# Step 1: Stop all running containers (optional)
docker stop $(docker ps -aq)

# Step 2: Remove old image
docker rmi -f instagramapi-web

# Step 3: Build the Docker image
docker build -t instagramapi-web .


