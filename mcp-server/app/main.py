from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Root endpoint (homepage)
@app.get("/")
def home():
    return {"message": "MCP Crypto Server Running Successfully!"}

# Include API routes
app.include_router(router)
