from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Model

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


@app.get("/")
async def root():
    return {"이즈나": "안아주도노"}


@app.post("/write")
async def write(data: Model):
    return "작성 완료"


@app.get("/items/")
async def read_item(limit: int = 10):
    return


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
