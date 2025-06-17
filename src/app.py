from typing import AsyncGenerator
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse
from src.config.connection import init_db
from src.routes import userRoutes
from src.utils.response import APIException
from src.config.settings import settings

PORT = settings.port or 8000


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    print(f"🔄 Server running on http://localhost:{PORT}")
    init_db()
    yield
    print("🛑 Shutting down...")


app = FastAPI(lifespan=lifespan)

app.get("/", tags=["Root"])(
    lambda: {"message": "Welcome to Swasthi Backend with Docker !!"}
)


@app.exception_handler(APIException)
async def api_exception_handler(request: Request, exc: APIException) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content=exc.detail)


# Register routes
app.include_router(userRoutes.router)
