from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from typing import List

from src.database import SessionLocal, engine
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

import environ
env = environ.Env()

# read the .env file
environ.Env.read_env()

# .env values
SECRET_KEY = env("SECRET_KEY")
ALGORITHM = env("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(env("ACCESS_TOKEN_EXPIRE_MINUTES"))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
