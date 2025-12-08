## Run Application with Docker

Build and start all services using Docker Compose:

```bash
docker-compose up --build

http://localhost:8000

Healthcheck: 

http://localhost:8000/health

Swagger API documentation:

http://localhost:8000/docs

To stop all containers:

docker-compose down

Run Tests Locally

pytest

Kubernetes Run

Make sure Kubernetes is running:

kubectl get nodes

Apply all Kubernetes manifests:

kubectl apply -f k8s/


Check running pods:

kubectl get pods


Check deployments:

kubectl get deployments


Check services:

kubectl get svc

Access Application in Kubernetes

If NodePort is used, get the application URL with:

minikube service backend-service --url


Or access directly in the browser:

http://localhost:30081/health
http://localhost:30081/docs

Environment Variables

Example environment variables used in the project:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=app_db
DB_USER=admin
DB_PASSWORD=admin

.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── db.py
├── tests/
│   └── test_health.py
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   └── configmap.yaml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md

CI Pipeline

The project uses GitHub Actions for continuous integration:

Install dependencies

Run unit tests with pytest

Build Docker image

The pipeline runs automatically on every push or pull request to the main branch.

Tech Stack

Backend: FastAPI

Database: PostgreSQL

Testing: Pytest

Containerization: Docker, Docker Compose

Orchestration: Kubernetes

CI: GitHub Actions
