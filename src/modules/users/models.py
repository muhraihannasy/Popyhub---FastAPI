from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, relationship

from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True)
    company_id = mapped_column(ForeignKey('companies.id'), nullable=False)
    name  = mapped_column(String(100), nullable=False)
    email  = mapped_column(String(100), unique=True, nullable=False)
    password = mapped_column(String(255), nullable=False)
    company = relationship('Company', back_populates='users')
