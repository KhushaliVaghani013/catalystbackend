from sqlalchemy.orm import Session
import models

def create_quote(db: Session, data, file_path=None):
    quote = models.GetQuote(**data.dict(), file_upload=file_path)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote


def get_all_quotes(db: Session):
    return db.query(models.GetQuote).all()











# from sqlalchemy.orm import Session
# import models, schemas
#
# # CREATE
# def create_quote(db: Session, quote: schemas.GetQuoteCreate):
#     print("Hello")
#     db_quote = models.GetQuote(**quote.dict())
#     db.add(db_quote)
#     db.commit()
#     db.refresh(db_quote)
#     return db_quote
#
#
# # READ ALL
# def get_quotes(db: Session):
#     return db.query(models.GetQuote).all()
#
#
# # READ ONE
# def get_quote(db: Session, quote_id: int):
#     return db.query(models.GetQuote).filter(models.GetQuote.id == quote_id).first()



# -------------------------------------------------------------------------

# def create_quote(data: schemas.GetQuoteCreate, db: Session = Depends(get_db), file_path):
#     stmt = insert(models.GetQuote).values(**data.dict(), file_upload=file_path)
#
#     result = db.execute(stmt)
#     db.commit()
#
#     return {
#         "status": "success",
#         "inserted_id": result.inserted_primary_key[0]
#     }
#
# def get_quotes(db: Session):
#     return db.query(models.GetQuote).all()