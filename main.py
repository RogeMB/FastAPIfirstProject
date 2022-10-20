import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def print_hi():
    return {'data': {'name': 'Roge'}}


@app.get('/about')
def about():
    return {'data': 'about page'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
