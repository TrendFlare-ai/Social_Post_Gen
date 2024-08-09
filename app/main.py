from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import generate
from models.model_loader import load_model


model = None

# Function to load the model
def load_model_first():
    global model
    model = load_model()
    print("Model loaded successfully.")

# Function to unload the model (if necessary)
def unload_model():
    global model
    model = None
    print("Model unloaded.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model_first()  # Load the model during startup
    yield
    unload_model()  # Clean up resources during shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Include routers after the model is loaded
app.include_router(generate.router)
