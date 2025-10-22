from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple file-based storage (replace with Azure Cosmos DB in production)
COUNTER_FILE = "visitor_count.json"


def get_visitor_count():
    """Read visitor count from file"""
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            data = json.load(f)
            return data.get("count", 0)
    return 0


def save_visitor_count(count):
    """Save visitor count to file"""
    with open(COUNTER_FILE, "w") as f:
        json.dump({"count": count}, f)


class VisitorCount(BaseModel):
    count: int


@app.get("/")
def read_root():
    return {"message": "Resume Challenge API"}


@app.get("/api/counter", response_model=VisitorCount)
def get_counter():
    """Get current visitor count"""
    count = get_visitor_count()
    return {"count": count}


@app.post("/api/counter", response_model=VisitorCount)
def increment_counter():
    """Increment visitor count"""
    count = get_visitor_count()
    count += 1
    save_visitor_count(count)
    return {"count": count}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
