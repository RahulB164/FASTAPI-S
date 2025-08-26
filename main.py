
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get():
    return {"message": "Welcome to the FastAPI application!"}







