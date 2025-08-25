from fastapi import FastAPI
from pydantic import BaseModel
import models
from database import engine
app = FastAPI()

models.Base.metadata.create_all(engine)

class blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create_blog(request: blog):
    return f'title {request.title} body {request.body}'
 
  