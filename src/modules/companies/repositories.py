from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.config import COMPANY_CODE_PREFIX
from .models import Company
from .schemas import CompanyCreate


class CompanyRepository:
    def __init__(self, db: Session):
        self.db = db

    def generate_company_code(self):
        last_company = self.db.query(Company.code).order_by(Company.code.desc()).first()

        code = f"{COMPANY_CODE_PREFIX}-"

        if last_company is not None:
            last_company_code = last_company[0]
            number = int(last_company_code.split("-")[1]) + 1
            code = f"{code}{number:06}"
        else:
            code = f"{code}{1:06}"

        return code

    def create_company(self, data: CompanyCreate):

        try:
            payload = Company(**data)

            self.db.add(payload)
            self.db.commit()
            self.db.refresh(payload)

            return payload
        except SQLAlchemyError as err:
            self.db.rollback()

            raise ValueError(f"An error occurred while creating:  {str(err)}")
