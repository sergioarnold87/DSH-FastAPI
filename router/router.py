from unittest import result
from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
#from schema.user_schema import UserSchema, DataUser
from config.db import engine
#from model.users import users
#from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()

@user.get("/")
def root():
  return {"message": "Hi, I am FastAPI with a router"}


@user.get("/api/drivers")
def get_drivers():
  with engine.connect() as conn:
    result = conn.execute(drivers.select()).fetchall() 

    return result

 