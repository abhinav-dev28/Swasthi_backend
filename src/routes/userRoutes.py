from fastapi import APIRouter
from src.models.employee import Employee
from src.controllers import employeeController as controller
from typing import Generic, TypeVar, Optional, List
from pydantic.generics import GenericModel

router = APIRouter(prefix="/employee", tags=["Employee"])

T = TypeVar("T")


class APIResponse(GenericModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T]


@router.post("/createEmployee", response_model=APIResponse[Employee])
def create_employee(data: Employee):
    return controller.addEmployee(data)


@router.get("/getAll", response_model=APIResponse[List[Employee]])
def list_employees():
    return controller.getAllEmployees()


@router.put("/update/{id}", response_model=APIResponse[Employee])
def update_employees(id: int, data: Employee):
    return controller.updateEmployee(id, data)


@router.get("/get/{id}", response_model=APIResponse[Employee])
def get_employee(id: int):
    return controller.getEmployee(id)
