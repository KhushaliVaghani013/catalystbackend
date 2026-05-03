from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from websockets import connect
import pyodbc

DATABASE_URL = "mssql+pyodbc://@KHUSHI\\SQLEXPRESS01/Catalyst?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
print("Data base connect successfully")

Base = declarative_base()
print("Data base connect successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



# DATABASE_URL = "sqlite:///./test.db"
