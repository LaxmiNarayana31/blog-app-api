from fastapi import FastAPI, Depends, status, HTTPException
from database import engine, SessionLocal, get_db
import schemas as schemas
from models import User,Blog
from database import Base
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import List
from routers import blog, user, authentication


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)