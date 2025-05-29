from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.config.connection import init_db
from src.routes import userRoutes  # update with your actual routes
from src.config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔄 Starting up...")
    # print("DB URL:", settings.database_url)
    init_db()  # Create tables
    yield
    print("🛑 Shutting down...")


app = FastAPI(lifespan=lifespan)

app.get("/", tags=["Root"])(lambda: {"message": "Welcome to the FastAPI Example!"})

# Register routes
app.include_router(userRoutes.router)
