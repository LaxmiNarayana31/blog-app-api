# SQLAlchemy Models
from pydantic import BaseModel
from database import Base 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(50))
    body = Column(String(100))
    
    user_id = Column(Integer, ForeignKey('users.id'))    # relationships between columns of two tables 
    creator = relationship('User', back_populates= 'blogs')




# create new user
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates='creator')