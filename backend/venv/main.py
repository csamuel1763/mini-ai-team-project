from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Mini AI Team Project Backend is Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }