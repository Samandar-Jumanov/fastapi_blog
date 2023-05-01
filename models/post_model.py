from sqlalchemy import Column , String , Integer , DateTime
from helpers.database import Base 
from pydantic import BaseModel
from datetime import datetime

class PostModel(Base):
    __tablename__ = 'posts'
    id = Column (Integer , primary_key = True , index = True)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp = Column(DateTime , default=datetime.utcnow) 


class PostSchema(BaseModel):
    title : str
    content : str 
    creator : str 


class PostOutput(BaseModel):
    title : str
    content : str 
    creator : str 

    class Config:
        orm_mode = True


