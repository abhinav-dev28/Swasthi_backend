# import uvicorn
# from src.config.settings import settings

# PORT = settings.port or 8000

# print(f"Server running on http://localhost:{PORT}")


# def start():
#     uvicorn.run("src.app:app", host="0.0.0.0", port=PORT, reload=True)


import subprocess
from watchfiles import run_process


def command():
    print("🔍 Running mypy type check...")
    mypy_result = subprocess.run(["mypy", "src"])

    if mypy_result.returncode == 0:
        print("✅ Type check passed. Starting server...")
        subprocess.run(
            [
                "uvicorn",
                "src.app:app",
                "--host",
                "0.0.0.0",
                "--port",
                "8000",
                "--reload",
            ]
        )
    else:
        print("❌ Type check failed. Fix errors to start the server.")


def start_dev():
    run_process("src", target=command, watch_filter=None)
