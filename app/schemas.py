from pydantic import BaseModel
from typing import Optional

#schema when you want to create a user info in the payload
class User(BaseModel):

                            
    name : str       
    email: str
    password : str 

#schema when user is print in console
class UserOut(BaseModel):

    name :str
    email:str
    

    class Config:
        orm_mode = True



#schema when user want to create a order info in the payload
class OrderCreation(BaseModel):
    item : str
    quantity : int
     


class Item(BaseModel):
    name: str
    price: int


#schema to view post information 
class OrderOut(BaseModel):
    
    item : int     
    price: int
    owner_id: int 

    class Config:
        orm_mode = True


#schema to login 
class Login(BaseModel):

    email: str
    password: str


class tokenData(BaseModel):
    id:Optional[str] = None



