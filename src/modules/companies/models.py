from sqlalchemy import String, Integer
from sqlalchemy.orm import  mapped_column, relationship

from src.database import Base

class Company(Base):
    __tablename__ = 'companies'

    id= mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False)
    code = mapped_column(String(30), unique=True, nullable=False)
    users = relationship( 'User', back_populates='company')

