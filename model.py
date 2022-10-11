from pydantic import BaseModel


class Model(BaseModel): # 글쓰기 post interface
    title: str
    content: str
