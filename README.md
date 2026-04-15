# FastApi_10K_calls
# 🚀 FastAPI High Performance API (10K RPS Concept)

This project demonstrates how to build a high-performance FastAPI service using:

- Async programming (async/await)
- Event loop concurrency
- Non-blocking I/O
- Parallel execution using asyncio.gather
- Load testing using autocannon

---

---

## Running the Server

### Run with multiple workers (multi-core usage)

  #### uvicorn app:app --workers 4 --port 8001
  
## API Endpoints
Endpoint	Description
#### /	Basic root endpoint
#### /fast	High-speed response (baseline performance)
#### /wait	Simulates async I/O using sleep
#### /parallel	Demonstrates parallel API calls
