from sqlalchemy.orm import Session
import models 
import schemas
from fastapi import HTTPException, status
from models import Blog

def get_all(db: Session):
    blogs =  db.query(models.Blog).all()
    return blogs



def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(
        title=request.title,
        body=request.body
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    



def update(id:int, request: schemas.BlogUpdate, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")

    if request.title and request.title!=None and request.title!="":
        blog.title = request.title
    
    if request.body and request.body!=None and request.body!="":
        blog.body = request.body
    
    db.commit()
    db.refresh(blog)
    return blog




def show(id:int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    
    return blog




def delete(id:int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
    
    db.delete(blog)
    db.commit()
    return blog