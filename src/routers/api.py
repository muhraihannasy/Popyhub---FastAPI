from fastapi import APIRouter

from ..config import ROUTE_PREFIX_V1

from ..modules.companies.routers import router as company_router

router = APIRouter()

def include_api_router():
    router.include_router(company_router, prefix=ROUTE_PREFIX_V1)

include_api_router()