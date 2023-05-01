from helpers.database import connect_db, SessionLocal
from models.post_model import PostOutput, PostSchema
from fastapi import APIRouter, Depends, status, UploadFile, File, HTTPException
import random 
import string 
from sqlalchemy.orm import Session 
from controller.post_controller import create_new, get_all, delete
import shutil
db = SessionLocal()


router = APIRouter(
    prefix='/posts',
    tags=['Post Tag']
)

@router.post('/create', status_code = status.HTTP_201_CREATED)
def create_post(post:PostSchema,db:Session = Depends(connect_db) ):
    return create_new(post ,  db )


@router.get('/getall', status_code = status.HTTP_200_OK)
def get(db : Session = Depends(connect_db)):
    return get_all(db)

@router.delete('/delete/{id}', status_code = status.HTTP_201_CREATED)
def delete_post(id :int , db:Session = Depends(connect_db)):
    return delete(id , db)


#post images 

@router.post('/image')
def upload_image(image : UploadFile=File(...) , db : Session = Depends(connect_db)) :
   try:
        letter = string.ascii_letters
        random_str = ''.join(random.choice(letter) for i in range(6))
        new = f'_{random_str}'
        filename = new.join(image.filename.rsplit('.', 1))
        path = f'images/{filename}'
        with open(path , 'w+b') as buffer:
           shutil.copyfileobj(image.file, buffer )
        db.add(filename)
        db.commit()
        db.refresh(filename)
        return {'filename':path}
        

   except Exception as error:
       raise  HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error)




