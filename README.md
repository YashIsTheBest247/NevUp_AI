# NevUp Backend – System of Record

## Overview
This project implements the backend system for NevUp's AI Trading Coach. It handles trade ingestion, behavioral analytics, and metrics computation using an asynchronous architecture.

---

## Architecture

Client → FastAPI → Redis Queue → Celery Worker → PostgreSQL

---

## Features

- Idempotent trade ingestion API
- Async behavioral analytics pipeline
- JWT-based authentication & tenancy enforcement
- Precomputed metrics for fast reads
- Dockerized full stack

---

### Flow

1. Client sends trade data via API  
2. Trade is stored in PostgreSQL (source of truth)  
3. Async task is pushed to Redis queue  
4. Celery worker processes behavioral metrics  
5. Metrics are stored for fast retrieval  

---

## Tech Stack

- **FastAPI** – High-performance API  
- **PostgreSQL** – Reliable database  
- **Redis** – Message broker  
- **Celery** – Async processing  
- **Docker** – Containerized setup  
- **k6** – Load testing  

---

## Features

- Idempotent trade ingestion (`tradeId`)
- Async behavioral analytics pipeline
- JWT-based authentication & multi-tenancy
- Precomputed metrics for fast reads
- Dockerized full stack

---

## Authentication

All endpoints require JWT authentication.
Authorization: Bearer <your_token>

---

## API Endpoints

### ➤ POST `/trades`
Create a trade (idempotent)

### ➤ GET `/users/{user_id}/metrics`
Retrieve behavioral metrics

---

## Metrics Implemented

- Plan adherence score  
- Revenge trading detection  
- Session tilt index  
- Win rate by emotional state  
- Overtrading detection  

---

## Setup

### 1. Run system

```bash
docker-compose up --build
```
---
## API Documentation
```bash
http://localhost:8000/docs
```
---
## Load Test
```bash
k6 run load-test.js
```
---
## Load Test Result
```bash
- ~120 requests/sec sustained
- 0% failure rate
- p95 latency ~800ms
- Tested up to 100 concurrent users

Note: Results are from local Docker environment.
```
---
## Project Structure
```bash 
backend/
  ├── models/
  ├── routes/
  ├── services/
  ├── workers/
  ├── database.py
  ├── main.py
  ├── seed.py

data/
  └── nevup_seed_dataset.csv

docker-compose.yml
Dockerfile
load-test.js
README.md
DECISIONS.md
```
---
## Design Philosophy
1. Async-first architecture
2. Precomputed metrics for fast reads
3. Strong consistency via PostgreSQL
4. Simple and scalable system design
---
## Future Improvements
1. Kafka for large-scale streaming
2. Redis caching layer
3. DB read replicas
4. ML-based behavioral scoring
---
