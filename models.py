from sqlalchemy import Column, Integer, String
from database import Base

class GetQuote(Base):
    __tablename__ = "getquote"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    service = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    material = Column(String, nullable=False)
    file_upload = Column(String, nullable=True)  # file path
