from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import *
from ..models.user import *
from ..schemas import *
from ..oauth2 import *

router = APIRouter()


@router.post('/login')
def login(payload:Login ,db:Session = Depends(get_db)):

    user = db.query(UserDb).filter(UserDb.email == payload.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    token = create_access_token(data={"user_id":user.id})    




    return token
