from fastapi import HTTPException
from typing import Any, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse


# def standard_response(
#     status_code: int,
#     success: bool,
#     data: Optional[Any] = None,
#     message: Optional[str] = None,
# ) -> JSONResponse:
#     return JSONResponse(
#         status_code=status_code,
#         content={
#             "success": success,
#             "message": message,
#             "data": jsonable_encoder(data),
#         },
#     )


def success_response(
    message: str = "Success", data: Optional[Any] = None, status_code: int = 200
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"success": True, "message": message, "data": jsonable_encoder(data)},
    )


class APIException(HTTPException):
    def __init__(
        self,
        message: str,
        code: str = "ERROR",
        status_code: int = 500,
        details: Optional[str] = None,
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "success": False,
                "message": message,
                "error": {"code": code, "details": details},
            },
        )
