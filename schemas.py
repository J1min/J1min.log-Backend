from sqlalchemy import Column, String, DateTime, Integer
from typing import Optional
from pydantic import BaseModel

import datetime

# "comments"
# "contact"
# "certificate"
# "careers"
# "leads"
# "skills"
# "prizes"
# "projects"


class info(BaseModel):
    user_id = int
    nickname = str
    blog = str
    github = str

    class Config:
        orm_mode = True


class board(BaseModel):
    board_id = int
    content = str
    created_at = datetime.datetime
    board_nickname = str
    user_id = int

    class Config:
        orm_mode = True


class photos(BaseModel):
    photo_id = int
    href = str
    board_id = int

    class Config:
        orm_mode = True


class script(BaseModel):
    script_id = int
    script_content = str
    author = str

    class Config:
        orm_mode = True
