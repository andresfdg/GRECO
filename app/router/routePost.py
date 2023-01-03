from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import *
from ..models.post import *
from ..schemas import *
from ..oauth2 import *
from typing import List
import psycopg2 
from psycopg2.extras import RealDictCursor

#database conection
conn = psycopg2.connect(host='localhost',database='greco',port='5432', user='postgres',password='2405', cursor_factory=RealDictCursor)
cur = conn.cursor()

#routers
router = APIRouter()

# get all users
@router.get("/post")                
def getusers(db:Session = Depends(get_db),current_user: int = Depends(get_user)):

    cur.execute("""  SELECT * FROM orders LEFT JOIN items ON orders.item = items.id  """)
    orders = cur.fetchall()

    #posts = db.query(OrderDb,ItemsDb).filter(OrderDb.item == ItemsDb.id).all()
    #result = db.query(OrderDb).join(UserDb, OrderDb.owner_id == UserDb.id, isouter=True)
    #print(result)
    return orders

#create a order an asigned to a gremio
@router.post("/post/create")
def hello(payload:OrderCreation,db:Session = Depends(get_db),current_user: int = Depends(get_user)):

    

    gre = db.query(NumericalGuiel).filter(NumericalGuiel.item == payload.item)

    
    #this if is use to comprobate if a gremio exist for the order product
    if not gre.first():
        gremio = NumericalGuiel(item = payload.item)

        db.add(gremio)
        db.commit()
        db.refresh(gremio)
        new_post = OrderDb(owner_id=current_user.id,gield_id=gremio.id  ,**payload.dict()) 

    #if the gremio exist increment the order_number     
    else:   #gre = gremio in database
        x = gre.first()    
        x.order_number = x.order_number + 1
        new_post = OrderDb(owner_id=current_user.id,gield_id=x.id  ,**payload.dict()) 
    #new order created
    
       
    
        
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


#get how many items were buy by all users
@router.get("/totalquantity/{id}")
def total(id:int, db:Session = Depends(get_db)):

    cur.execute(f"  SELECT SUM(quantity) FROM orders WHERE item ={str(id)} ")

    count = cur.fetchone()

    return count


#get how many orders exist for a consulted item 
@router.get("/totalitem/{id}")
def total(id:int, db:Session = Depends(get_db)):

    cur.execute(f"  SELECT COUNT(item) FROM orders WHERE item ={str(id)} ")

    count = cur.fetchone()

    return count


@router.get("/prueba/{id}")
def prueba(id:int):

    cur.execute(f"""SELECT orders WHERE item = {str(id)} """)

    return "working"


    
#RETURN ALL GIELD AND THEIR ORDERS
@router.get("/join")
def prueba():

    cur.execute(f""" SELECT * FROM orders LEFT JOIN numericalguiel ON orders.gield_id = numericalguiel.id ORDER BY numericalguiel.id """)
    orders = cur.fetchall()

    return orders


 

