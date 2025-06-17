from typing import Any
from fastapi import HTTPException
from src.models.employee import Employee
from sqlmodel import Session, select
from src.utils.response import APIException, success_response


def get_employee_by_id(session: Session, id: int) -> Any:
    try:
        employee = session.get(Employee, id)

        if not employee:
            raise APIException(
                message="Employee not found", code="EMPLOYEE_NOT_FOUND", status_code=404
            )

        return success_response(
            "Employee fetched successfully", data=employee, status_code=200
        )

    except APIException as e:
        raise e  # Let FastAPI handle this using your custom exception handler

    except Exception as e:
        raise APIException(
            message="Internal Server Error",
            code="UNEXPECTED_ERROR",
            status_code=500,
            details=str(e),
        )


def add_employee(session: Session, data: Employee) -> Any:
    try:
        new_employee = Employee(**data.model_dump())
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)

        # Return successful response
        return success_response(
            message="Employee created successfully",
            status_code=201,
            # data=employee).model_dump(),
        )

    except Exception as e:
        raise APIException(
            message="Failed to create employee",
            code="EMPLOYEE_CREATION_FAILED",
            status_code=500,
            details=str(e),
        )


def updateEmployee(session: Session, id: int, data: Employee) -> Any:
    try:
        employee = session.get(Employee, id)
        if not employee:
            raise APIException(
                message="Employee Not found", code="EMPLOY_NOT_FOUND", status_code=404
            )

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(employee, key, value)

            session.add(employee)
            session.commit()
            session.refresh(employee)

        return success_response(
            "Employee updated successfully", data=employee, status_code=200
        )

    except HTTPException as e:
        raise e  # Let existing HTTPException pass through

    except Exception as e:
        raise APIException(
            message="Internal Server Error",
            code="UNEXPECTED_ERROR",
            status_code=500,
            details=str(e),
        )


def getAllEmployees(session: Session) -> Any:
    try:
        statement = select(Employee)
        results = session.exec(statement).all()

        if not results:
            return APIException(
                message="No employees found", code="NO_EMPLOYEE_FOUND", status_code=404
            )

        return success_response(
            "List of employees",
            data=results,
            status_code=200,
        )
    except HTTPException as e:
        raise e  # Let existing HTTPException pass through

    except Exception as e:
        raise APIException(
            message="Internal Server Error",
            code="UNEXPECTED_ERROR",
            status_code=500,
            details=str(e),
        )
