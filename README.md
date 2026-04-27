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
http://localhost:8000/docs

---
## Load Test
```bash
k6 run --summary-trend-stats="avg,min,max,p(90),p(95)" load-test.js
```
---

## 🧪 Load Testing Results (k6), Detailed Analysis Run

Load testing was performed using **k6** with staged traffic (up to 100 concurrent users).

---

### Summary

- **Total Requests:** 4351  
- **Throughput:** ~85 req/sec  
- **Failure Rate:** 0%  
- **Successful Checks:** 100%  

---

### Latency Metrics

| Metric    | Value    |
|-----------|----------|
| Average   | 539.6 ms |
| Minimum   | 10.33 ms |
| Maximum   | 2.07 s   |
| p90       | 1.24 s   |
| p95       | 1.39 s   |

---

### Execution

- **Iterations:** 4351  
- **Virtual Users (VUs):** up to 100  
- **Test Duration:** ~50 seconds  
- **No interrupted iterations**

---

### Network

- **Data Received:** 631 kB (~12 kB/s)  
- **Data Sent:** 3.1 MB (~61 kB/s)  

---

### Observations

- System handled concurrent load with **0% failure rate**
- Stable throughput under increasing load
- Latency increased at higher concurrency (expected in local Docker setup)
- Architecture remains **reliable and scalable**

---
> Note: Results are based on a local Docker environment. Production deployment with optimized infrastructure would yield lower latency and higher throughput.
---

## Load Testing Result (Basic Run)
```bash
k6 run load-test.js
```
## Results
- Total Requests: 6304
- Throughput: ~124 req/sec
- Failure Rate: 0%
- Successful Checks: 100%

## Latency Metrics
```bash
| Metric  | Value   |
| ------- | ------- |
| Average | 368 ms  |
| Minimum | 8.47 ms |
| Maximum | 1.29 s  |
| p90     | 730 ms  |
| p95     | 811 ms  |
```
---

## Execution Details
- Iterations: 6304
- Virtual Users (VUs): up to 100
- Test Duration: ~50 seconds
- No interrupted iterations
---

## Network Usage
- Data Received: 914 kB (~18 kB/s)
- Data Sent: 4.5 MB (~89 kB/s)
---
## Observations
- System handled concurrent load with 0% failure rate
- Sustained ~124 requests/sec
- Stable performance across increasing load stages
- Latency remained under ~800ms (p95) under 100 concurrent users
- Async architecture ensured non-blocking request handling
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
