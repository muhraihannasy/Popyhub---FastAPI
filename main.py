from fastapi import FastAPI

from src.config import API_PREFIX
from src.database import engine, Base
from src.routers.api import router as router_api

# models
from src.modules.users import models
from src.modules.companies import models

def get_application() -> FastAPI:

    ## Start FastApi App
    application = FastAPI()

    ## Generate Database Tables
    Base.metadata.create_all(bind=engine)

    ## Mapping Api Routes
    application.include_router(router_api, prefix=API_PREFIX)

    return application

app = get_application()
