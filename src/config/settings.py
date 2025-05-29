from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(override=True)  # ✅ This forces .env to override system env


class Settings(BaseSettings):
    pg_user: str
    pg_password: str
    pg_host: str
    pg_port: int
    pg_db: str
    port: int = 8000

    class Config:
        env_file = ".env"

    @property
    def db_url(self):
        from sqlalchemy.engine import URL

        return URL.create(
            drivername="postgresql+psycopg2",
            username=self.pg_user,
            password=self.pg_password,
            host=self.pg_host,
            port=self.pg_port,
            database=self.pg_db,
            query={"sslmode": "require"},
        )


settings = Settings()
