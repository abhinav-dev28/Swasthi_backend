from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(override=True)  # ✅ This forces .env to override system env


class Settings(BaseSettings):
    database_url: str
    port: int = 8000
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    class Config:
        env_file = ".env"


settings = Settings()
