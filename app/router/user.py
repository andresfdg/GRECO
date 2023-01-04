from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import *
from ..models.user import *
from ..schemas import *
from ..oauth2 import *
from typing import List
from passlib.context import CryptContext

#calls CryptContext and allows to create hash and incriptate data
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

# create new user
@router.post("/user/create", response_model=UserPrint)
def create_user(payload:CreateUser, db:Session = Depends(get_db)):
    #create a hash for the password
    passhash = pwd_context.hash(payload.password)
    payload.password = passhash

    #create a user using the payload information
    new_user = UserDb(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)   

    return new_user   
#---------------------------------------------------------------------------------------
# get all users
@router.get("/user",response_model=List[UserPrint])               
def root(db:Session = Depends(get_db), current_user: int = Depends(get_user)):
    #get all users registered in the dataset
    users = db.query(UserDb).all()
    
    return users

#----------------------------------------------------------------------------------------
@router.post("/storeuser/create", response_model=UserPrint)
def store_user_create(payload:CreateStoreUser, db:Session = Depends(get_db)):
    #create a hash for the password
    passhash = pwd_context.hash(payload.password)
    payload.password = passhash

    #create a user using the payload information
    new_user = StoreUserDb(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)   

    return new_user      