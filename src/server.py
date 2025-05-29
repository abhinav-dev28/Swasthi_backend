from src.app import init_app as app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=True)
