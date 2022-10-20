from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog?limit=10&published=true')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit}: published blogs from the db'}
    else:
        return {'data': f'{limit}: blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


# los path dinámicos deben ir después de los estáticos

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return limit


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=9000, reload=True)
