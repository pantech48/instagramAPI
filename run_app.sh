#!/bin/bash


# Ask for Instagram credentials
read -p "Please enter your Instagram username or press Enter to use the default: " username
read -sp "Please enter your Instagram password or press Enter to use the default: " password
echo

# If the user entered a username and password, export them as environment variables
if [ -n "$username" ]
then
    export INSTAGRAM_USERNAME=$username
fi
if [ -n "$password" ]
then
    export INSTAGRAM_PASSWORD=$password
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker is not installed. Please install Docker first."
    exit
fi

# Check if docker image already exists
if [ "$(docker images -q instagramapi-web 2> /dev/null)" == "" ]; then
  echo "Building Docker Image"
  ./build.sh
else
  echo "Docker Image already exists"
fi

# Run docker-compose up
cd docker
echo "Starting application..."
docker compose up
