from datetime import date
from pydantic import BaseModel


class EmployeeOut(BaseModel):
    id: int
    name: str
    position: str
    salary: float
    created_at: date

    class Config:
        orm_mode = True
