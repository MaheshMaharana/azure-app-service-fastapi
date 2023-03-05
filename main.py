from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "<h1>This is a REST API for enabling my ML model to be used by other services.</h1>"

@app.get("/users")
def getUsers():
    return [
        {
            "name": "roshi",
            "id": 1
        },
        {
            "name": "else",
            "id": 2
        }
    ]
