from fastapi import FastAPI
from .schemas import *
from .database import *
from .router import routeUser,routePost,auth

Base.metadata.create_all(bind=engine)




app = FastAPI()

app.include_router(routeUser.router)
app.include_router(routePost.router)
app.include_router(auth.router)











