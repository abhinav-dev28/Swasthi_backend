from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(override=True)  # ✅ This forces .env to override system env


class Settings(BaseSettings):
    database_url: str
    pg_user: str
    pg_password: str
    pg_host: str
    pg_port: int
    pg_db: str
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
