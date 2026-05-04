import re
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator


class GetQuoteCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service: Optional[str] = None
    quantity: int
    material: str

    @field_validator("phone")
    def validate_phone(cls, v):
        if v is None:
            return v

        # Remove spaces / + sign
        cleaned = re.sub(r"[^\d]", "", v)

        if not (5 <= len(cleaned) <= 15):
            raise ValueError("Phone number must be between 5 and 15 digits")

        return v

    @field_validator("email")
    def validate_email_domain(cls, v):
        if not v.endswith(".com"):
            raise ValueError("Email must end with .com")
        return v

class GetQuoteResponse(GetQuoteCreate):
    id: int
    file_upload: Optional[str] = None

    class Config:
        from_attributes = True
