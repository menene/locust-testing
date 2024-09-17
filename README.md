
# Load and Stress Test Sample API

This project demonstrates a simple Express API, containerized with Docker, designed to serve as a sample application for load and stress testing using [Locust](https://locust.io/). The project includes:

- A simple Express API
- A Locust testing environment to simulate load
- Docker and Docker Compose configuration to orchestrate the environment

## Project Structure

```plaintext
load-stress-sample-api/
├── app/
│   ├── package.json        # Express API package definition
│   ├── index.js            # Express API entry point
├── docker-compose.yml       # Docker Compose configuration for API and Locust
├── dockerfiles/
│   ├── api/
│   │   └── Dockerfile       # Dockerfile for building the API container
│   └── locust/
│       └── Dockerfile       # Dockerfile for building the Locust container
└── locust/
    ├── locustfile.py        # Locust test file defining API load tests
    └── requirements.txt     # Python requirements for Locust
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

To build and run both the API and Locust testing environment, simply run the following commands:

```bash
docker-compose up --build
```

This command will:
- Build and start the Express API on `http://localhost:3000`.
- Build and start the Locust load testing tool, which will be accessible on `http://localhost:8089`.

### Accessing the API

Once the containers are running, you can access the Express API at:

- **Base URL**: `http://localhost:3000`
- **Available Endpoints**:
  - `GET /`: Returns a welcome message.
  - `POST /echo`: Echoes back the JSON data sent in the request body.

Example:
```bash
curl http://localhost:3000/
```

```bash
curl -X POST http://localhost:3000/echo -H "Content-Type: application/json" -d '{"message": "Hello from Locust"}'
```

### Accessing Locust

Locust is a tool used to perform load and stress testing on the API. You can access the Locust web interface by navigating to:

- **URL**: [http://localhost:8089](http://localhost:8089)

#### Running a Test in Locust

From the Locust web interface:
1. Enter the **number of users** to simulate.
2. Enter the **spawn rate** (how many users per second).
3. Set the **host** to `http://api:3000` (this points to the Express API).
4. Click **Start Swarming** to begin the test.

#### Example Locust Configuration:
- **Number of Users**: 100
- **Spawn Rate**: 10 (users per second)
- **Host**: `http://api:3000`

### Locust Test Definition

The Locust test is defined in the `locust/locustfile.py`. This file includes simple tasks that hit two endpoints:
- A `GET` request to `/` (the root endpoint).
- A `POST` request to `/echo` with a sample payload.

```python
from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_index(self):
        self.client.get("/")

    @task
    def test_echo(self):
        self.client.post("/echo", json={"message": "Hello from Locust"})
```

### Stopping the Application

To stop the containers, run:

```bash
docker-compose down
```

## About Locust

[Locust](https://locust.io/) is an easy-to-use, distributed load testing tool that can help test the performance of web applications by simulating multiple users. Locust provides a web UI for setting parameters like user count and spawn rate, and it also allows you to define user behaviors and requests in Python.

Key features:
- Simulates large numbers of users hitting your application.
- Supports distributed and scalable testing.
- Provides real-time feedback on response times and performance metrics.

For more information on Locust, visit the [official Locust documentation](https://docs.locust.io/).

## License

This project is open-source and available under the [MIT License](LICENSE).
