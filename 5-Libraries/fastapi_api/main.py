"""
Simple FastAPI api
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
def greet_user(name: str):
    """
    Greet the user with the name provided
    """
    return {"Hello": name}
