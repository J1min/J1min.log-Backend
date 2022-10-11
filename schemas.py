from sqlalchemy import Column, String, DateTime, Integer
from typing import Optional
from pydantic import BaseModel


# "board"
# "comments"
# "contact"
# "prizes"
# "careers"
# "leads"
# "projects"
# "certificate"
# "skills"



class info(BaseModel):
    user_id = int
    nickname = str
    blog = str
    github = str

    class Config:
        orm_mode = True
