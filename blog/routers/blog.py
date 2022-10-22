from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, database
from blog.repository import blog
from blog.schemas import Blog


router = APIRouter(prefix='/blog', tags=['blogs'])


@router.get(path='', status_code=200, response_model=List[schemas.ShowBlog])
def all_(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post(path='', status_code=status.HTTP_201_CREATED, response_model=Blog)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)


@router.delete(path='/{id_}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id_: int, db: Session = Depends(database.get_db)):
    return blog.destroy(id_, db)


@router.put(path='/{id_}', status_code=status.HTTP_202_ACCEPTED)
def update(id_: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id_, request, db)


@router.get('/blog/{id_}', status_code=200, response_model=schemas.ShowBlog)
def show(id_: int, db: Session = Depends(database.get_db)):
    return blog.show(id_, db)
