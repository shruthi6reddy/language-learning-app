from fastapi import FastAPI
import app.models  # noqa — ensures all models are registered

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from backend"}
