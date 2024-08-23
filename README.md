# Flask Redis Docker Demo App

This project demonstrates a simple Flask application integrated with Redis, and it's containerized using Docker. The app tracks the number of visits to the home route using Redis.

## Project Structure

- `myapp.py`: The main Flask application.
- `Dockerfile`: Dockerfile to build the container image.
- `docker-compose.yml`: Docker Compose file to set up and run the Flask and Redis services.
- `requirements.txt`: Python dependencies for the Flask application.

## Features

- **Flask Application**: Provides a home route that returns a JSON response with a visit count.
- **Redis Integration**: Tracks the number of visits using Redis as a cache.
- **Docker**: Containerizes the application for easy deployment.

## Prerequisites

- Docker and Docker Compose installed on your machine.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://YeabTesfaye/flask-redis-demo.git
   cd flask-redis-dem
   ```

2. **Create `requirements.txt`**
Ensure requirements.txt includes the necessary dependencies:

```bash
  flask 
  redis
```

3.**Build and Run with Docker Compose**
Build and start the services using Docker Compose:

```bash
docker-compose up --build
```

This command will:

Build the Docker image for the Flask application.
Start both the Flask application and Redis services.

4.**Access the Application**
Once the containers are up and running, you can access the Flask application at:

```bash 
http://localhost:5000

```

## Dockerfile

The Dockerfile for building the Flask application image:

## docker-compose.yml

The `docker-compose.yml` file for defining the services:





