from sqlmodel import SQLModel, create_engine
from src.config.settings import settings

connection_string: str = str(settings.database_url).replace(
    "postgres", "postgresql+psycopg2"
)

engine = create_engine(
    connection_string,
    connect_args={"sslmode": "require"},
    pool_recycle=300,
    pool_size=5,
    echo=True,
)
print("Database engine created with URL:", settings.database_url)


def init_db():
    try:
        print("Initializing the database...")
        SQLModel.metadata.create_all(engine)
        print("Database initialized successfully.")
    except Exception as e:
        print("An error occurred while initializing the database:", e)
