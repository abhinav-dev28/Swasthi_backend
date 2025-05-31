import uvicorn
from src.config.settings import settings

PORT = settings.port or 8000


def start():
    uvicorn.run("src.app:app", host="0.0.0.0", port=PORT, reload=True)
