from sqlmodel import SQLModel, create_engine
from src.config.settings import settings

# print("OG connection :", settings.database_url)

engine = create_engine(
    settings.database_url,
    connect_args={"sslmode": "require"},
    pool_recycle=300,
    pool_size=5,
    # echo=True,     used for debugging, can be removed in production
)
# print("Database engine created with URL:", settings.database_url)


def init_db():
    try:
        print("Connecting to DB...")
        SQLModel.metadata.create_all(engine)
        print("DB Connected")
    except Exception as e:
        print("An error occurred while initializing the database:", e)
