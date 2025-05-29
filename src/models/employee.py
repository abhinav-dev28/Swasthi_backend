from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class EmployeeBase(SQLModel):
    name: str
    position: str
    salary: float


class Employee(EmployeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(SQLModel):
    name: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
