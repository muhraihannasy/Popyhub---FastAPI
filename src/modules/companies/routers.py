from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.depedencies import get_db_session
from src.exceptions import ErrorResponse
from . import schemas, services

router = APIRouter(
    prefix="/companies",
    tags=['companies']
)

@router.post('/', status_code=201)
def create_company(data: schemas.CompanyCreateRequest, db: Session = Depends(get_db_session)):
    service = services.CompanyService(db)

    try :
        result = service.create_company(data)

        return {
            "success": True,
            "data": result
        }

    except ValueError as err:
        return ErrorResponse(status_code=500, message=str(err))

