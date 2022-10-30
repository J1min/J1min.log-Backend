from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
import boto3

import os, uuid, json, random

from interface import model, schemas

import database
from dotenv import load_dotenv


model.Base.metadata.create_all(bind=database.engine)


app = FastAPI()
load_dotenv()

origins = [
    os.environ.get("FRONT_BASE_URL"),
    os.environ.get("FRONT_DEV_URL"),
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
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


def post_db(db, data):
    db.add(data)
    db.commit()
    db.refresh(data)


@app.get("/")
def get_user():
    return {"code": 200, "response": "연결 성공"}


@app.get("/user/{user_id}")  # 특정 유저 조회
def get_user(user_id: int, db: Session = Depends(get_db)):
    users = db.query(model.info).filter(model.info.user_id == user_id).first()
    return {"code": 200, "response": "유저가 있어요", "userData": users}


@app.get("/board/all")  # 전체 게시글 조회
def get_all_board(db: Session = Depends(get_db)):
    board = (
        db.query(model.board).order_by(model.board.board_id.desc()).all()
    )  # .limit(5).all()
    return {"code": 200, "response": "게시글이 있어요", "boardData": board}


@app.get("/board/{board_id}")  # 특정 게시글 조회
def get_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(model.board).filter(model.board.board_id == board_id).first()
    return {"code": 200, "response": "게시글이 있어요", "boardData": board}


@app.get("/script/all")
def get_all_script(db: Session = Depends(get_db)):
    script = db.query(model.script).all()
    return {"code": 200, "response": "명언이 있어요", "scriptData": script}


@app.get("/script/random")
def get_all_script(db: Session = Depends(get_db)):
    script = db.query(model.script).all()
    randomNumber = random.randint(0, len(script) - 1)
    result = {
        "script_content": script[randomNumber].script_content,
        "author": script[randomNumber].author,
    }
    return {"code": 200, "response": "명언이 있어요", "scriptData": result}


@app.get("/script/{script_id}")  # 특정 명언 조회
def get_script(script_id: int, db: Session = Depends(get_db)):
    script = db.query(model.script).filter(model.script.script_id == script_id).first()
    return {"code": 200, "response": "명언이 있어요", "scriptData": script}


@app.get("/user/leads/all")  # leads 조회
def get_leads(db: Session = Depends(get_db)):
    userData = db.query(model.leads).all()
    return {"code": 200, "response": "전송 완료", "userData": userData}


@app.post("/script")  # 명언 작성
def post_board(body: schemas.script, db: Session = Depends(get_db)):
    scriptData = model.script(script_content=body.script_content, author=body.author)
    post_db(db, scriptData)
    return {"code": 200, "response": "추가 완료", "Data": scriptData}


@app.post("/write")  # 게시글 작성
def post_board(body: schemas.board, db: Session = Depends(get_db)):
    boardData = model.board(
        content=body.content,
        created_at=body.created_at,
        board_title=body.board_title,
        user_id=body.user_id,
        thumbnail=body.thumbnail,
        description=body.description,
    )
    post_db(db, boardData)
    return {"code": 200, "response": "전송 완료", "boardData": boardData}


def upload_file(fileName, file):
    s3 = boto3.resource("s3")
    s3.Bucket(os.environ.get("AWS_BUCKET_NAME")).put_object(
        Key=fileName, Body=file, ContentType="image/jpeg"
    )
    return


@app.post("/photo")  # 사진 post
async def upload_photo(file: UploadFile, db: Session = Depends(get_db)):
    content = await file.read()
    href = f"{str(uuid.uuid4())}.jpeg"  # uuid로 유니크한 파일명으로 변경
    upload_file(href, content)
    photoData = model.photos(href=href, board_id=1)
    post_db(db, photoData)
    return photoData


@app.post("/user/leads")  # 게시글 작성
def post_leads(body: schemas.leads, db: Session = Depends(get_db)):
    userData = model.leads(
        lead_name=body.lead_name,
        started_at=body.started_at,
        ended_at=body.ended_at,
        user_id=1,
    )
    post_db(db, userData)
    return {"code": 200, "response": "전송 완료", "userData": userData}
