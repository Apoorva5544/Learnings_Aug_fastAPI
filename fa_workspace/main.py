from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':  'blog list'}

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
