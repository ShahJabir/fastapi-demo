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


@app.get("/items")
def read_items():
    """Read the items endpoint."""
    return {"items": ["item1", "item2", "item3"]}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Read a specific item by ID."""
    return {"item_id": item_id}
