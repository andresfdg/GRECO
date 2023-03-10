from fastapi import FastAPI
from .schemas import *
from .database import *
from .router import order, auth, user, item, store

#create the database
Base.metadata.create_all(bind=engine)

#aplication runs
app = FastAPI()

#route is used for create the users and get how many users exist
app.include_router(user.router)

#route is used for login users
app.include_router(auth.router)

#route is used for order management 
app.include_router(order.router)

#route is used for item management 
app.include_router(item.router)

app.include_router(store.router)













