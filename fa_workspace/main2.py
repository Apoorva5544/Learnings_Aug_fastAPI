from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/blog')
def index(limit,published:bool = True, sort: Optional[str] = None):
    #only get 10 published blogs 
    # return published
    return {'data': f'{limit} blogs from the database' }

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):#define int id
    #fetch blogs by id
    return {'data': id}


@app.get('/blog/{id}/comments')
#fetch comments for blogs with id = id 
def comments(id: int): 
    return {'data': {'1','2'}}
