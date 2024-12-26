from sqlalchemy.orm import Session

from .repositories import CompanyRepository
from .schemas import CompanyCreateRequest

class CompanyService:
    def __init__(self, db: Session):
        self.repository = CompanyRepository(db)

    def create_company(self, data: CompanyCreateRequest):
        code = self.repository.generate_company_code()

        company = {
            "name": data.name,
            "code": code
        }

        return self.repository.create_company(company)
