from typing import Generator
from sqlmodel import SQLModel, Session, create_engine
from src.config.settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={"sslmode": "require"},
    pool_recycle=300,
    pool_size=5,
    # echo=True,     used for debugging, can be removed in production
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    try:
        print("Connecting to DB...")
        SQLModel.metadata.create_all(engine)
        print("DB Connected")
    except Exception as e:
        print("An error occurred while initializing the database:", e)
