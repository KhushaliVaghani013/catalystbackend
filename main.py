from fastapi import FastAPI
from database import Base, engine
import getquote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Catalyst API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


# Create table
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(getquote.router)

