from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.config.connection import get_session
from src.controllers import employeeController as controller
from typing import Any, List, Optional
from sqlmodel import Session

from src.models.employee import Employee
from src.schemas.employee import EmployeeOut

router = APIRouter(prefix="/employee", tags=["Employee"])

# T = TypeVar("T")


class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None


@router.post("/createEmployee", response_model=APIResponse)
def create_employee(data: Employee, session: Session = Depends(get_session)) -> Any:
    return controller.add_employee(session, data)


@router.get("/getAll", response_model=List[EmployeeOut])
def list_employees(session: Session = Depends(get_session)) -> Any:
    return controller.getAllEmployees(session)


@router.put("/update/{id}", response_model=EmployeeOut)
def update_employees(
    id: int, data: Employee, session: Session = Depends(get_session)
) -> Any:
    return controller.updateEmployee(session, id, data)


@router.get("/get/{id}", response_model=EmployeeOut)
def get_employee(id: int, session: Session = Depends(get_session)) -> Any:
    return controller.get_employee_by_id(session, id)
