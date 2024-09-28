# Video Livestream Platform

## Author
1. Trieu Ngoc Tam

- Email: tamtn.dynamite.work@gmail.com

- GitHub: trieungoctam

- MSV: B21DCCN658

2. Hoang Quoc Anh

- Email: 

- GitHub: 

- MSV: B21DCCN146

3. Dinh Hoang Anh

- Email: 

- GitHub: 

- MSV: B21DCCN142

## Overview
This project demonstrates how to build a microservice architecture using FastAPI (Python) and Spring Boot (Java). The project consists of two independent services:

- FastAPI Backend: A simple API service built using FastAPI.
- Spring Boot Service: Another service built with Spring Boot.

Both services are containerized using Docker, and they can be run together using Docker Compose. Each service can function independently but communicates via REST or can be extended to communicate using gRPC for higher efficiency.

## Project Structure
```bash

/fastapi-springboot-project
│
├── fastapi-backend/                  # FastAPI microservice
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── routes.py         # FastAPI routes
│   │   ├── core/
│   │   │   ├── config.py             # Configurations
│   │   ├── db/
│   │   │   ├── models.py             # Database models
│   │   ├── main.py                   # Entry point for FastAPI
│   ├── Dockerfile                    # Docker configuration for FastAPI
│   ├── requirements.txt              # Python dependencies
│   └── README.md                     # FastAPI documentation
│
├── springboot-service/               # Spring Boot microservice
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/
│   │   │   │   │   ├── example/
│   │   │   │   │   │   ├── SpringbootServiceApplication.java # Main Spring Boot file
│   │   │   │   │   │   ├── controller/
│   │   │   │   │   │   │   ├── ApiController.java            # API routes
│   ├── pom.xml                        # Maven dependencies
│   ├── Dockerfile                     # Docker configuration for Spring Boot
│   └── README.md                      # Spring Boot documentation
│
├── docs/                             # Documentation folder
│   ├── basic_theory.md               # Basic theory behind address methods
│   ├── architecture.md               # System architecture documentation
│   ├── api_docs.md                   # API documentation for FastAPI and Spring Boot
│   ├── grpc_docs.md                  # gRPC integration documentation
│   ├── deployment.md                 # Deployment strategies and options
│   └── troubleshooting.md            # Troubleshooting and common issues
│
├── docker-compose.yml                 # Docker Compose to run both services
└── README.md                          # Project-level documentation
```
## Documentation
Here are links to the detailed documentation for this project:

- [Basic Theory](/docs/basic_theory.md): Basic theory and concepts behind address method (Unicast, Broadcast, Multicast, Anycast).
- [Architecture Documentation](/docs/architechture.md): Learn more about the overall system architecture, communication patterns, and design decisions.
- [API Documentation](docs/api_docs.md): Find detailed descriptions of the API endpoints, request/response formats, and usage examples for both FastAPI and Spring Boot services.
- [gRPC Integration](docs/grpc_docs.md): Learn how to extend the system to use gRPC for faster and more efficient communication between services.
- [Deployment Strategies](docs/deployment.md): Review strategies for deploying this project in different environments (local, cloud, Kubernetes).
- [Troubleshooting Guide](docs/troubleshooting.md): Common issues and their solutions for both services.

## Prerequisites

- **Docker** and **Docker Compose** installed on your machine.

- **Python 3.9+** for FastAPI development (optional if using Docker).

- **Java 11+** for Spring Boot development (optional if using Docker).

## Installation and Running the Project
1. Clone the repository
```bash
git clone https://github.com/your-repo/fastapi-springboot-project.git
cd fastapi-springboot-project
```
2. Run both services with Docker Compose
- The project includes a docker-compose.yml file that helps you easily run both services.

```bash
docker-compose up --build
```
3. Access the services
- FastAPI Backend: The FastAPI service will be accessible at http://localhost:8000. You can use endpoints like /users:

```bash
http://localhost:8000/users
```
- Spring Boot Service: The Spring Boot service will be accessible at http://localhost:8080. For example, you can use the /api/users endpoint:

```bash
http://localhost:8080/api/users
```
4. Stopping the services
- To stop the services, use the following command:

```bash
docker-compose down
```

## FastAPI Service Details
FastAPI is a modern web framework for building APIs with Python. It is designed for high-performance applications and is extremely easy to use.

### API Endpoints
- GET /users: Returns a list of users.
### Running FastAPI without Docker
If you want to run the FastAPI service without Docker, follow these steps:

1. Navigate to the fastapi-backend/ directory.
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```
## Spring Boot Service Details
Spring Boot is a widely-used Java framework for building web services and microservices with robust configuration and high scalability.

### API Endpoints
- GET /api/users: Returns a list of users from Spring Boot.
### Running Spring Boot without Docker
If you want to run the Spring Boot service without Docker, follow these steps:

1. Navigate to the springboot-service/ directory.
2. Build the project using Maven:
```bash
mvn clean install
```
3. Run the Spring Boot server:
```bash
mvn spring-boot:run
```
## Docker Compose Configuration
In the docker-compose.yml, both services are connected in a single network to ensure they can communicate with each other.

```yaml
version: '3'
services:
  fastapi-backend:
    build: ./fastapi-backend
    ports:
      - "8000:8000"
    networks:
      - app-network

  springboot-service:
    build: ./springboot-service
    ports:
      - "8080:8080"
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
```
## Testing
FastAPI: You can run unit tests using pytest for FastAPI:
```bash
pytest
```
Spring Boot: You can run unit tests using JUnit in Spring Boot:
```bash
mvn test
```
## Extending the Project
- gRPC Integration: You can extend this project by adding gRPC communication between the FastAPI and Spring Boot services for faster inter-service communication.
- Database Support: Add database support (PostgreSQL, MySQL) to each service to store and manage persistent data.
- Authentication: Add JWT-based authentication or OAuth2 to secure the services.
License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

- Fork the repository.

- Create your feature branch (git checkout -b feature/my-feature).

- Commit your changes (git commit -am 'Add my feature').

- Push to the branch (git push origin feature/my-feature).

- Create a new Pull Request.
