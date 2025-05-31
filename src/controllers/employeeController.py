from src.models.employee import Employee
from src.config.connection import engine
from sqlmodel import Session, select
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse


def addEmployee(data: Employee):
    try:
        with Session(engine) as session:
            employee = Employee(**data.model_dump())
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={
                    "success": True,
                    "message": "Employee Added",
                    "data": employee,  # ✅ FIXED
                },
            )
    except Exception as e:
        return JSONResponse(
            status_code=status.e.status_code,
            content={
                "success": False,
                "message": f"An error occurred while adding the employee: {str(e)}",
            },
        )


def updateEmployee(id: int, data: Employee):
    try:
        with Session(engine) as session:
            employee = session.get(Employee, id)
            print("Employee fetched:", employee)

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

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "message": "Employee Updated",
                    "data": employee,  # ✅ FIXED
                },
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
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    data="No employees found",
                )
            return {"success": True, "message": "List of employees", "data": results}
    except HTTPException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=e.detail,
        )


def getEmployee(id: int):
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
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "success": True,
                    "message": "Employee fetched",
                    "data": employee,
                },
            )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "message": f"An error occurred while getting     the employee: {str(e)}",
            },
        )
