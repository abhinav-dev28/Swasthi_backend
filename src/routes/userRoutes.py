from src.controllers import userController
from fastapi import APIRouter
from src.models.employee import Employee, EmployeeCreate, EmployeeUpdate
from src.controllers import employeeController as controller
from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, List
from pydantic.generics import GenericModel

router = APIRouter(prefix="/users", tags=["Users"])

T = TypeVar("T")


class APIResponse(GenericModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T]


@router.get("/", response_model=userController.IGetAllUsers)
def get_users():
    return userController.getAllUsers()


@router.post("/createEmployee", response_model=APIResponse[Employee])
def create_employee(data: EmployeeCreate):
    return controller.addEmployee(data)


@router.get("/getAll", response_model=APIResponse[List[Employee]])
def list_employees():
    return controller.getAllEmployees()


@router.put("/update/{id}")
def update_employees(id: int, data: EmployeeUpdate):
    return controller.updateEmployee(id, data)
