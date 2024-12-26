from fastapi.responses import JSONResponse

def ErrorResponse(status_code: int, message: str):
    response = {
        "status": False,
        "data": {
            "error": {
                "message": message
            }
        }
    }


    return JSONResponse(
        status_code=status_code,
        content=response
    )