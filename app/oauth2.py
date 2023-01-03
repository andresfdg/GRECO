from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .database import *
from .models.user import *
from .schemas import*

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    token = jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)



    return token
    

def verify_access_token(token: str, credentials_exception):

    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

    id = payload.get("user_id")

    if id is None:
        raise credentials_exception

    token_data = tokenData(id = id)

    return token_data


def get_user(token: str = Depends(oauth2_schema),db:Session = Depends(get_db) ):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    tk = verify_access_token(token,credentials_exception)

    user = db.query(UserDb).filter(UserDb.id == tk.id).first()

    return user



