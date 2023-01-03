from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import *
from ..models.user import *
from ..schemas import *
from ..oauth2 import *
from typing import List

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



            



router = APIRouter()


@router.get("/user",response_model=List[UserOut])                # get all users
def root(db:Session = Depends(get_db),current_user: int = Depends(get_user)):

    users = db.query(UserDb).all()

    return users

#---------------------------------------------------------------------------------------
                                                   # create new user


@router.post("/user/create", response_model=UserOut)
def user(payload:User, db:Session = Depends(get_db)):

    passhash = pwd_context.hash(payload.password)
    payload.password = passhash


    new_user = UserDb(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)

 
   

    return new_user   