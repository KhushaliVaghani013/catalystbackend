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
    countryCode: str = Form(...),
    phone: str = Form(None),
    service: str = Form(...),
    quantity: int = Form(...),
    material: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    print("API HIT ✅")

    full_phone = None
    if phone:
        full_phone = f"{countryCode}{phone}"

    file_path = None

    if file and file.filename:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file_path = file_path.replace("\\", "/")

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    data = schemas.GetQuoteCreate(
        name=name,
        email=email,
        phone=full_phone,
        service=service,
        quantity=quantity,
        material=material
    )

    quote = crud.create_quote(db, data, file_path)

    return quote
except Exception as e:
        print("ERROR:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
    # try:
    #
    # except Exception as e:
    #     print("ERROR ❌:", e)
    #     raise HTTPException(status_code=500, detail=str(e))

    # return {"status": "success", "message": "Data created successfully", "data": quote}

# ✅ GET API
# @router.get("/quotes/", response_model=list[schemas.GetQuoteResponse])
@router.get("/quotes/", response_model=None)
def get_all_quotes(db: Session = Depends(get_db)):
    return crud.get_all_quotes(db)






# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import SessionLocal
# import crud, schemas
#
# router = APIRouter(prefix="/quotes", tags=["Quotes"])
#
#
# # DB Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# # CREATE API
# @router.post("/")
# def create_quote(quote: schemas.GetQuoteCreate, db: Session = Depends(get_db)):
#     return crud.create_quote(db, quote)
#
#
# # GET ALL API
# @router.get("/")
# def get_all_quotes(db: Session = Depends(get_db)):
#     return crud.get_quotes(db)
#
#
# # GET SINGLE API
# @router.get("/{id}")
# def get_single_quote(id: int, db: Session = Depends(get_db)):
#     return crud.get_quote(db, id)


# ----------------------------------------------












# CREATE (Normal JSON)
# @router.post("/")
# def create_quote(quote: schemas.GetQuoteCreate, db: Session = Depends(get_db)):
#     return crud.create_quote(db, quote)



# ✅ READ ONE
# @router.get("/quotes/{quote_id}", response_model=schemas.GetQuoteResponse)
# def read_quote(quote_id: int, db: Session = Depends(get_db)):
#     quote = crud.get_quote(db, quote_id)
#     if not quote:
#         raise HTTPException(status_code=404, detail="Quote not found")
#     return quote


# FILE UPLOAD API  ✅ ADD HERE
# @router.post("/file upload/")
# def upload_quote(
#     name: str,
#     email: str,
#     phone_no: str,
#     services: str,
#     quantity: int,
#     material: str,
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):
#     # create uploads folder if not exists
#     if not os.path.exists("uploads"):
#         os.makedirs("uploads")
#
#     file_location = f"uploads/{file.filename}"
#
#     # save file
#     with open(file_location, "wb") as f:
#         f.write(file.file.read())
#
#     # save data in DB
#     quote_data = schemas.GetQuoteCreate(
#         name=name,
#         email=email,
#         phone_no=phone_no,
#         services=services,
#         quantity=quantity,
#         material=material,
#         file_upload=file_location
#     )
#
#     return crud.create_quote(db, quote_data, file_location)
