from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id_: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id_)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id_} is not found')

    blog.delete(synchronize_session='fetch')
    db.commit()
    return 'Blog is deleted'


def update(id_: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id_)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id_} is not found')

    blog.update(request)
    db.commit()
    return 'updated successfully'


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not longer available')
    return blog
