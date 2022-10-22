import uvicorn
from fastapi import FastAPI
from blog import models
from blog.database import engine
from routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)


@app.get(path='/')
def index():
    return {'This is Index:', 'Go to /docs to test the app'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', port=9000, reload=True)
