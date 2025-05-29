from sqlmodel import SQLModel, create_engine
from src.config.settings import settings

engine = create_engine(settings.db_url, echo=True)
print("Database engine created with URL:", settings.db_url)


def init_db():
    try:
        print("Initializing the database...")
        SQLModel.metadata.create_all(engine)
        print("Database initialized successfully.")
    except Exception as e:
        print("An error occurred while initializing the database:", e)
