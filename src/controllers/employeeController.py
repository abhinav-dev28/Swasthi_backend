from src.models.employee import Employee
from src.config.connection import engine
from sqlmodel import Session, select
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from src.utils.response import standard_response as standard


def addEmployee(data: Employee):
    try:
        with Session(engine) as session:
            employee = Employee(**data.model_dump())
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return standard(
                status_code=status.HTTP_201_CREATED,
                success=True,
                message="Employee Added",
                data=employee,
            )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "message": f"An error occurred while adding the employee: {str(e)}",
            },
        )


def updateEmployee(id: int, data: Employee):
    try:
        with Session(engine) as session:
            employee = session.get(Employee, id)

            if not employee:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={
                        "success": False,
                        "message": "Employee Not found",
                    },
                )

            for key, value in data.model_dump(exclude_unset=True).items():
                setattr(employee, key, value)

            session.add(employee)
            session.commit()
            session.refresh(employee)

            return standard(
                status_code=status.HTTP_200_OK,
                success=True,
                message="Employee Updated",
                data=employee,
            )

    except HTTPException as e:
        raise e  # Let existing HTTPException pass through

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while updating the employee: {str(e)}",
        )


def getAllEmployees():
    try:
        with Session(engine) as session:
            statement = select(Employee)
            results = session.exec(statement).all()

            if not results:
                return standard(
                    status_code=404, success=False, message="No employees found"
                )

            return standard(
                status_code=200,
                success=True,
                message="List of employees",
                data=results,
                # data=[emp.model_dump() for emp in results],
            )
    except Exception as e:
        return standard(
            status_code=500, success=False, message=f"Something went wrong: {str(e)}"
        )


def getEmployee(id: int):
    try:
        with Session(engine) as session:
            employee = session.get(Employee, id)
            if not employee:
                return standard(
                    status_code=status.HTTP_404_NOT_FOUND,
                    success=False,
                    message="Employee not found",
                )
            return standard(
                status_code=status.HTTP_200_OK,
                success=True,
                message="Employee found",
                data=employee,
            )

    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": f"An error occurred while getting     the employee: {str(e)}",
            },
        )
