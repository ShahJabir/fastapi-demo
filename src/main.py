"""Basic fastapi program"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Read the root endpoint."""
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    """Read the health endpoint."""
    return {"status": "healthy"}
