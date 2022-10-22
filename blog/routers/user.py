from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas, database
from blog.repository import user

router = APIRouter(prefix="/user", tags=['users'])


@router.post(path='', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get(path='', response_model=schemas.ShowUser)
def get_user(id_user: int, db: Session = Depends(database.get_db)):
    return user.show(id_user, db)
