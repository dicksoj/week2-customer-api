README.md (Week 2 Customer API)
# Week 2 – Customer API with Postgres & Docker Compose

This project demonstrates a simple REST API with FastAPI and PostgreSQL, containerized using Docker Compose.

## Features
- **Python FastAPI** application exposing REST endpoints
- **Postgres database** initialized with schema + synthetic customer data
- **Docker Compose** orchestration
- **Healthcheck & CI/CD** with GitHub Actions

## Endpoints

- `GET /customers` → Returns all customers
- `GET /customers/{id}` → Returns one customer by ID

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/week2-customer-api.git
cd week2-customer-api


### 2. Start the stack
docker-compose up --build


The API will be available at:
👉 http://localhost:8000/customers

### 3. Example Query
curl http://localhost:8000/customers/1

### 4. Stop containers
docker-compose down

## Testing

Run tests locally with:

```bash
pytest -v tests

Project Structure

### week2-customer-api/                ← Project root
├── app/                           ← FastAPI application
│   ├── main.py                    ← FastAPI endpoints
│   ├── generate_customers.py      ← Script to populate DB
│   ├── Dockerfile                 ← Builds customer_api container
│   └── db/                        ← Database files
│       └── init.sql               ← Table schema (Postgres initialization)
│
├── tests/                         ← API test suite
│   └── test_api.py                ← Pytest tests for endpoints
│
├── docker-compose.yml              ← Orchestrates DB + API services
├── requirements.txt                ← Python dependencies (FastAPI, psycopg2, pytest, etc.)
└── .github/
    └── workflows/
        └── ci.yml                 ← GitHub Actions workflow for CI
