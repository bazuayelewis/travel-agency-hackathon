from fastapi import FastAPI
import uvicorn
from routers.api_routes import router

app = FastAPI(
    title="Travel Agency Hackathon API",
    version="1.0.0",
    description="API for the Travel Agency Hackathon project"
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"root": "Travel Agency Project"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)