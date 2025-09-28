from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Literal
import uvicorn

app = FastAPI(title="Test API Server", version="1.0.0")


@app.post("/")
async def root():
    return {"message": "Test API Server is running on port 8002", "status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(
        "server2:app",
        host="localhost",
        port=8002,
        reload=True
    )