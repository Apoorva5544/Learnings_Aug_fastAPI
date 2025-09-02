from fastapi import FastAPI, Depends , status, Response , HTTPException
from pydantic import BaseModel
import models
from typing import List
from . import hashing
from database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

#models.Base.metadata.drop_all(bind=engine) 
models.Base.metadata.create_all(engine)

class blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


class user(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code = status.HTTP_201_CREATED)
def create_blog(request: blog,db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

@app.delete('/blog/{id}',status_code = status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog with {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id,request: blog,db:Session = Depends(get_db)):
    blog  = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog with {id} is not available")
    blog.update({'title': 'updated title', 'body': 'updated body'})
    db.commit()
    return 'updated'


@app.get('/blog',response_model=List[ShowBlog])
def all_blog(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code = 200,response_model=ShowBlog)
def show(id,response: Response,db:Session = Depends(get_db)): 
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with {id} is not available")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f'Blog with {id} is not available'}
    return blog 
   

@app.post('/user',response_model=ShowUser)
def create_user(request: user,db: Session = Depends(get_db)):
   
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
