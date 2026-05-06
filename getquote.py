import shutil, os
from fastapi import APIRouter, Depends, File, UploadFile, Form, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from utills import success_response

router = APIRouter(tags=["Quotes"])

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


#  CREATE API
@router.post("/createquotes/", response_model=schemas.GetQuoteResponse)
def create_quote(
    name: str = Form(...),
    email: str = Form(...),
    country_code: str = Form(...),
    phone: int = Form(None),
    service: str = Form(...),
    quantity: int = Form(...),
    material: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    print("API HIT ✅")

    file_path = None

    if file and file.filename:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file_path = file_path.replace("\\", "/")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    data = schemas.GetQuoteCreate(
        name=name,
        email=email,
        country_code=country_code,
        phone=str(phone),
        service=service,
        quantity=quantity,
        material=material
    )

    quote = crud.create_quote(db, data, file_path)

    return quote


# ✅ GET API
# @router.get("/quotes/", response_model=list[schemas.GetQuoteResponse])
@router.get("/quotes/", response_model=None)
def get_all_quotes(db: Session = Depends(get_db)):
    return crud.get_all_quotes(db)
