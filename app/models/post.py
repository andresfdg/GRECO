from sqlalchemy import Column, Integer, String, Boolean, ForeignKey , Float
from ..database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship 




class OrderDb(Base):
    __tablename__="orders"

    id = Column(Integer, primary_key = True, nullable=False)
    date = Column(TIMESTAMP(timezone=True),nullable=False,server_default = text('now()'))
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    item = Column(Integer, ForeignKey('items.id'))
    owner = relationship('UserDb')
    quantity = Column(Integer, nullable = False )
    gield_id = Column(Integer,  ForeignKey('numericalguiel.id'))
     
    

    
    

class ItemsDb(Base):
    __tablename__="items"

    id = Column(Integer , primary_key = True, nullable=False )
    name = Column(String, nullable=False)
    price = Column(Integer, nullable = False)


class NumericalGuiel(Base):
    __tablename__="numericalguiel"

    id = Column(Integer, primary_key = True, nullable=False)
    date = Column(TIMESTAMP(timezone=True),nullable=False,server_default = text('now()'))
    active = Column(Boolean, server_default='False',nullable = False)
    item = Column(Integer, ForeignKey('items.id'))
    order_number = Column(Integer, server_default= '1' )
    


    


