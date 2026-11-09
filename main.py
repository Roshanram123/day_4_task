
from fastapi import FastAPI

app = FastAPI()

# API 1: Welcome message
@app.get("/")
def home():
    return {
        "message": "Hello, FastAPI"
    }


# API 2: Greet user using URL parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello {name}, welcome to FastAPI!"
    }


@app.post("/postt")
def postt():
    response = {
        "message": "This is a POST request"
    }
    return response