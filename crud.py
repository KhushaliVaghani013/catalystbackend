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
