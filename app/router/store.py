from fastapi import APIRouter, Depends , status , HTTPException
from sqlalchemy.orm import Session
from ..database import *
from ..models.user import *
from ..models.ecommerceModels import *
from ..schemas import *
from ..oauth2 import *
from typing import List



router = APIRouter()

#create a new store
@router.post("/store/create")
def create_item(payload:StoreCreate, db:Session = Depends(get_db), current_user: int = Depends(get_user)):
    print(current_user.type)

    valide_store = db.query(StoreDb).filter(StoreDb.owner == current_user.id).first()

    if valide_store:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE ,detail=f'cuantas tiendas quieres care verga? ya tienes una!')

    if  current_user.type == 'Store':
        new_store = StoreDb(owner=current_user.id,**payload.dict())
        db.add(new_store)
        db.commit()
        db.refresh(new_store)
        print(new_store)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'NO PUEDES METER ESA MONDA')       

    return new_store 
#---------------------------------------------------------------------------------------
# get all users
@router.get("/store",response_model=List[ItemPrint])               
def get_item(db:Session = Depends(get_db),current_user: int = Depends(get_user)):
    #get all users registered in the dataset
    items = db.query(ItemDb).all()
    
    return items