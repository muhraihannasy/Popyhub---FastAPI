import os


from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USER = "root"
PASSWORD = "raihan2704"
DATABASE = "fastapi_pos"
HOST = "127.0.0.1"
PORT = 3306

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:raihan2704@127.0.0.1:3306/fastapi_pos'

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

