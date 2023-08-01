

# InstagramAPI

This is an API designed to fetch Instagram photos from user profiles using Selenium. It's packaged in a Docker container for easy deployment.

## Setup

The following steps will guide you through the setup process.

### 1. Clone the Repository

First, clone the repository from GitHub to your local machine. You can do this by running the following command:

```bash
git clone https://github.com/pantech48/instagramAPI.git
```

Once the repository has been cloned, navigate into the project directory:

```bash
cd instagramAPI
```

### 2. Install Docker

The next step is to install Docker. You can find the installation guide for different platforms in the links below:

- [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [Install Docker on Windows](https://docs.docker.com/docker-for-windows/install/)
- [Install Docker on Mac](https://docs.docker.com/docker-for-mac/install/)

### 3. Set Environment Variables

The API requires two environment variables: `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD`. These represent the Instagram credentials that the API will use to login and fetch photos.

You can provide these credentials as environment variables in your system:

```bash
export INSTAGRAM_USERNAME=your_instagram_username
export INSTAGRAM_PASSWORD=your_instagram_password
```

Replace `your_instagram_username` and `your_instagram_password` with your actual Instagram username and password.

If you do not provide these environment variables, the API will use default credentials specified in the Dockerfile.

### 4. Build Docker Image

After setting up Docker and the environment variables, run the `build.sh` script. This script will build a Docker image of the API.

You can run the script using the following command:

```bash
./build.sh
```

### 5. Navigate to Docker Directory

After building the Docker image, navigate to the Docker directory in the project:

```bash
cd docker
```

### 6. Run Docker Container

Inside the Docker directory, run the Docker container using Docker Compose:

```bash
docker compose up
```

This will start the API inside a Docker container.

## API Endpoints

The API has one endpoint:

- `GET /getPhotos/{username}`: Fetches Instagram photos from the user profile specified by `username`. You can also specify a `max_photo_count` (default=5) query parameter to limit the number of photos fetched. Example usage:

```bash
curl localhost:8080/instagram/getPhotos/johndoe?max_photo_count=10
```
---