from pydantic import BaseModel


class IGetAllUsers(BaseModel):
    success: bool
    message: str


def getAllUsers() -> IGetAllUsers:
    return IGetAllUsers(success=True, message="List of users")
