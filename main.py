from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

import os, uuid, json, random

from interface import model 
from interface import schemas

from database import SessionLocal, engine
from dotenv import load_dotenv


model.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    os.environ.get('FRONT_BASE_URL')
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


def post_db(db, data):
    db.add(data)
    db.commit()
    db.refresh(data)


@app.get("/user/{user_id}")  # 특정 유저 조회
def get_user(user_id: int, db: Session = Depends(get_db)):
    users = db.query(model.info).filter(model.info.user_id == user_id).first()
    return (
        {"response": "유저가 없는데요"}
        if users == None
        else {"response": "유저가 있어요", "userData": users}
    )


@app.get("/board/{board_id}")  # 특정 게시글 조회
def get_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(model.board).filter(model.board.board_id == board_id).first()
    return (
        {"response": "게시글이 없는데요"}
        if board == None
        else {"response": "게시글이 있어요", "boardData": board}
    )


@app.get("/script/all")
def get_all_script(db: Session = Depends(get_db)):
    script = db.query(model.script).all()
    return script


@app.get("/script/random")
def get_all_script(db: Session = Depends(get_db)):
    script = db.query(model.script).all()
    randomNumber = random.randint(0, len(script) - 1)
    result = {
        "script_content": script[randomNumber].script_content,
        "author": script[randomNumber].author,
    }
    return (
        {"response": "명언이 하나도 없는데요"}
        if script == None
        else {"response": "명언이 있어요", "scriptData": result}
    )


@app.get("/script/{script_id}")  # 특정 명언 조회
def get_script(script_id: int, db: Session = Depends(get_db)):
    script = (
        db.query(model.script).filter(model.script.script_id == script_id).first()
    )
    return (
        {"response": "명언이 없는데요"}
        if script == None
        else {"response": "명언이 있어요", "scriptData": script}
    )


@app.post("/script")  # 명언 작성
async def post_board(body: schemas.script, db: Session = Depends(get_db)):
    scriptData = model.script(script_content=body.script_content, author=body.author)
    post_db(db, scriptData)
    return {"response": "추가 완료", "Data": scriptData}


@app.post("/write")  # 게시글 작성
async def post_board(body: schemas.board, db: Session = Depends(get_db)):
    boardData = model.board(
        content=body.content,
        created_at=body.created_at,
        board_nickname=body.board_nickname,
        user_id=body.user_id,
    )
    post_db(db, boardData)
    return {"response": "전송 완료", "Data": boardData}


@app.post("/photo")  # 사진 post
async def upload_photo(file: UploadFile, db: Session = Depends(get_db)):
    UPLOAD_DIR = "./photo"
    content = await file.read()
    href = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    with open(os.path.join(UPLOAD_DIR, href), "wb") as fp:
        fp.write(content)  # 서버 로컬에 이미지 저장 (쓰기)
        photoData = model.photos(href=href, board_id=1)
    post_db(db, photoData)
    return photoData


@app.get("/get/photo/{photo_id}")  # 사진의 PK를 입력하면 해당 사진 return
async def download_photo(photo_id: int, db: Session = Depends(get_db)):
    UPLOAD_DIR = "./photo/"  # 사진 폴더 안에 저장
    find_photo = (
        db.query(model.photos).filter(model.photos.photo_id == photo_id).first()
    )
    return FileResponse(UPLOAD_DIR + find_photo.href)
