from fastapi import FastAPI
from app.routers import router
from app.database import create_connection


app = FastAPI(
    title="TrailService API",
    description="Microservice for managing trail data.",
    version="1.0.0"
)

# Include routers
app.include_router(router)

# Database connection test
@app.on_event("startup")
def startup_event():
    conn = create_connection()
    if conn:
        print("Database connected successfully.")
    else:
        print("Failed to connect to database.")


@app.get("/")
def root():
    return {"message": "TrailService API is running"}
