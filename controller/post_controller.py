from models.post_model import PostModel, PostSchema
from helpers.database import SessionLocal , connect_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
import datetime


db = SessionLocal()

def create_new(post:PostSchema, db: Session = Depends(connect_db)):
    post_new = PostModel(
        title = post.title,
        content = post.content,
        creator = post.creator,
    )

    if not post_new:
        raise HTTPException(status_code=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, detail='Please complete the tables')
    try:
        db.add(post_new)
        db.commit()
        db.refresh(post_new)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    return {"post":post_new}


def get_all(db : Session = Depends(connect_db)):
    all_posts = db.query(PostModel).all()
    try:
        return all_posts
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)



def delete(id : int , db : Session = Depends(connect_db)):
    post = db.query(PostModel).filter(PostModel.id == id ).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cannot find post')
    try:
        db.delete(post)
        db.commit()
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)
    return {"message":"Deleted post "}


