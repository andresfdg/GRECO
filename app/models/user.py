from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base


class UserDb(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    

    """ name = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    password = Column(String, nullable = False)
    birthdate = Column(String, nullable=False)
    city = Column(String, nullable=False)
    adress = Column(String, nullable=False)
    favoriteStore = Column(String, nullable=False)

 """