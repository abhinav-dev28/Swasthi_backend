from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    position: str = Field(index=True, max_length=50)
    salary: float = Field(ge=0, description="Salary must be a non-negative number")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# class Post(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str = Field(index=True, max_length=100)
#     content: str = Field(index=True)
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
