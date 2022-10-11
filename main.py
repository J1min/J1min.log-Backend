from fastapi import FastAPI
from sqlalchemy.orm import Session

from typing import List
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    try:
        print("okay db")
        db = SessionLocal()
        yield db
    finally:
        print("not okay db")
        db.close()


@app.get("/")
def main(db: Session = Depends(get_db)):
    users = db.query(models.info).all()
    return users


# @app.get("/users/", response_model=List[schemas.User])
# def show_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users


# @app.post("/users/", response_model=schemas.User)
# def create_users(enter: schemas.User, db: Session = Depends(get_db)):
#     user = models.User(
#         username=enter.username,
#         fullname=enter.fullname,
#         role=enter.role,
#         state=enter.state,
#     )
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user


# @app.put("/users/{user_id}", response_model=schemas.User)
# def update_users(
#     user_id: int, enter: schemas.UserUpdate, db: Session = Depends(get_db)
# ):
#     user = db.query(models.User).filter_by(id=user_id).first()
#     user.fullname = enter.fullname
#     db.commit()
#     db.refresh(user)
#     return user


# @app.delete("/users/{user_id}", response_model=schemas.response)
# def delete_users(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter_by(id=user_id).first()
#     db.delete(user)
#     db.commit()
#     response = schemas.response(message="Successfully removed!")
#     return response
