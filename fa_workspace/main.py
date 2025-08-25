from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name' : 'Apoorva'}}


@app.get('/about' )
def about():
    return {'data' : {'name' : 'Apoorva' , 'age' : 20}}

@app.get('/contact')
def contact():
    return {'data' : {'email' : 'apoorva.com'}}