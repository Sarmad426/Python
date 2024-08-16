"""
Simple FastAPI api
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
def greet_user(name: str):
    return {"Hello": name}