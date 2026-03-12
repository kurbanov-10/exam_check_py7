from fastapi import FastAPI

app=FastAPI()

@app.get('/hello/')
def hello():
    return{"hello": "world"}

# @app.get('/news/')
# def hello():
#     return{"result": ["news 1","news 2", "news 3"]}

new_data=[
    {"id": 1, "title": "news 1"},
    {"id": 2, "title": "news 2"},
    {"id": 3, "title": "news 3"},
    {"id": 4, "title": "news 4"},
    {"id": 5, "title": "news 5"},
    {"id": 6, "title": "news 6"},
    {"id": 7, "title": "news 7"},
    {"id": 8, "title": "news 8"}
]
@app.get('/news/')
def news( limit: int = None , query: str=None):
    
    if query:
        data=list(filter(lambda item: query in item['title'], new_data))
    else:
        data=new_data
        
    return data[:limit]

@app.get('/news/{news_id}')
def news_detail(news_id: int):
    return {"result": list(filter(lambda item: item['id'] == news_id, new_data))[0]}
