from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Microservice deployed successfully on Azure Container Apps!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
