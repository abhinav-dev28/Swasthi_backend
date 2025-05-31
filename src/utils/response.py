from fastapi.responses import JSONResponse
from typing import Any, Optional
from fastapi.encoders import jsonable_encoder


def standard_response(
    status_code: int,
    success: bool,
    data: Optional[Any] = None,
    message: Optional[str] = None,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "success": success,
            "message": message,
            "data": jsonable_encoder(data),
        },
    )
