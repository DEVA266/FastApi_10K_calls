from fastapi import FastAPI
import asyncio
import httpx # for external api

app = FastAPI()

# Global async HTTP client (connection pooling)
client = httpx.AsyncClient()

@app.get("/")
async def root():
    return {"message": "Root Message"}

#(baseline)
@app.get("/fast")
async def fast():
    return {"status": "ok"}

# I/O endpoint
@app.get("/waiting")
async def wait():
    await asyncio.sleep(0.01)
    return {"status": "done"}

# Parallel API calls using asyncio.gather
@app.get("/parallel")
async def parallel():
    r1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    r2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

    res1, res2 = await asyncio.gather(r1, r2)

    return {
        "todo1": res1.json(),
        "todo2": res2.json()
    }