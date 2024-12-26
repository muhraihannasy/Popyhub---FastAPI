from pydantic import BaseModel

class CompanyCreateRequest(BaseModel):
    name: str

class CompanyCreate(BaseModel):
    name: str
    code: str

class Company(BaseModel):
    id: int
    name: str
    code: str