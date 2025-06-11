from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.connection import init_db
from src.routes import userRoutes  # update with your actual routes
from src.config.settings import settings

PORT = settings.port or 8000


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"🔄 Server running on http://localhost:{PORT}")
    init_db()  # Create tables
    yield
    print("🛑 Shutting down...")


app = FastAPI(lifespan=lifespan)

app.get("/", tags=["Root"])(
    lambda: {"message": "Welcome to Swasthi Backend with Docker !!"}
)

# Register routes
app.include_router(userRoutes.router)
