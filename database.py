from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from websockets import connect
import pyodbc
import os


# Load .env file
load_dotenv()

# Get environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")


# hostinger
DATABASE_URL = (f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=280,
    pool_size=5,
    max_overflow=10,
    connect_args={
        "connect_timeout": 30
    }
)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
print("Data base connect successfully")

Base = declarative_base()
print("Data base connect successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
