from fastapi import FastAPI
from pydantic import BaseModel
import models
from database import engine
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(engine)

class blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create_blog(request: blog,db:Session):
    return db
 
  