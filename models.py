from sqlalchemy import Column, Integer, String
from database import Base

class GetQuote(Base):
    __tablename__ = "getquote"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    country_code = Column(String(50), nullable=False)
    phone = Column(String(50), unique=True, nullable=True)
    service = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    material = Column(String(255), nullable=False)
    file_upload = Column(String(255), nullable=True)  # file path
