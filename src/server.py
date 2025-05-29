from src.app import init_app as app
from src.config.settings import settings
import uvicorn

PORT = settings.port | 8000

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=PORT, reload=True)
