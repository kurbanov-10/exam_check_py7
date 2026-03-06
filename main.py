from fastapi import FastAPI

app=FastAPI()

@app.get('/hello/')
def hello():
    return{"hello": "world"}

@app.get('/news/')
def hello():
    return{"result": ["news 1","news 2", "news 3"]}