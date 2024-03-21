from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import List

from app.src.database import SessionLocal, engine
from sqlalchemy.orm import Session

from dotenv import load_dotenv
import os

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# .env values
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
