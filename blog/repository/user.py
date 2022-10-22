from sqlalchemy.orm import Session
from blog import hashing, models, schemas
from fastapi import status, HTTPException


def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email,
                           password=hashing.HashClass.encode_psw(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id_user: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id_user).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id_user} is not longer available')
    return user
