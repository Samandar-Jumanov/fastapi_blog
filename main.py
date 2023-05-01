from fastapi import FastAPI
from helpers.database  import connect_db, engine
from models import post_model
from routers.post_route import router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors  import  CORSMiddleware
app = FastAPI()

#db connection 
post_model.Base.metadata.create_all(engine)
connect_db()

app.include_router(router)
app.mount('/images', StaticFiles(directory='images'), name = 'images')
@app.get('/start')
def start_app():
    return {'message':'App started '}



#cors middleware 


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

