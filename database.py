from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from websockets import connect
import pyodbc



# hostinger
DATABASE_URL = "mysql+pymysql://u778110718_Khushi:Cattech9374@auth-db1951.hstgr.io:3306/u778110718_catalyst"


engine = create_engine(DATABASE_URL,pool_pre_ping=True,        # Tests connection before using it ✅
    pool_recycle=280,          # Recycle connections before MySQL times them out
    pool_size=5,
    max_overflow=10,
    connect_args={
        "connect_timeout": 30
    })

SessionLocal = sessionmaker(bind=engine)
print("Data base connect successfully")

Base = declarative_base()
print("Data base connect successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
