from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

import os, uuid, json

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
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/user/{user_id}")  # 특정 유저 조회
def get_user(user_id: int, db: Session = Depends(get_db)):
    users = db.query(models.info).filter(models.info.user_id == user_id).first()
    return (
        {"response": "유저가 없어요"}
        if users == None
        else {"response": "유저가 있어요", "userData": users}
    )


@app.get("/board/{board_id}")  # 특정 게시글 조회
def get_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(models.board).filter(models.board.board_id == board_id).first()
    return (
        {"response": "게시글이 없는데요"}
        if board == None
        else {"response": "게시글이 있어요", "BoardData": board}
    )


@app.post("/write/")  # 게시글 작성
async def post_board(body: schemas.board, db: Session = Depends(get_db)):
    print(body)
    print(body)
    print(body)
    print(body)
    boardData = models.board(
        content=body.content,
        created_at=body.created_at,
        board_nickname=body.board_nickname,
        user_id=body.user_id,
    )
    db.add(boardData)
    db.commit()
    db.refresh(boardData)
    return {"response": "전송 완료", "Data": boardData}


@app.post("/photo")  # 사진 post
async def upload_photo(file: UploadFile, db: Session = Depends(get_db)):
    UPLOAD_DIR = "./photo"
    content = await file.read()
    href = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    with open(os.path.join(UPLOAD_DIR, href), "wb") as fp:
        fp.write(content)  # 서버 로컬에 이미지 저장 (쓰기)
        photoData = models.photos(href=href, board_id=1)
        db.add(photoData)  # <models.photos object at 0x0000021B035C68E0>
        db.commit()
        db.refresh(photoData)
    return photoData


@app.get("/get/photo/{photo_id}")  # 사진의 PK를 입력하면 해당 사진 return
async def download_photo(photo_id: int, db: Session = Depends(get_db)):
    UPLOAD_DIR = "./photo/"  # 사진 폴더 안에 저장
    find_photo = (
        db.query(models.photos).filter(models.photos.photo_id == photo_id).first()
    )
    return FileResponse(UPLOAD_DIR + find_photo.href)
