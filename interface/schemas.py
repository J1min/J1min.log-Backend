from sqlalchemy import Column, String, DateTime, Integer
from typing import Optional
from pydantic import BaseModel


class info(BaseModel):
    nickname: str
    blog: str
    github: str

    class Config:
        orm_mode: True


class board(BaseModel):
    user_id: int
    created_at: str
    content: str
    board_nickname: str


class comments(BaseModel):
    board_id: int
    created_at: str
    content: str
    user_id: int

    class Config:
        orm_mode: True


class contact(BaseModel):
    phone_number: str
    phone_number: str
    user_id: int

    class Config:
        orm_mode: True


class prizes(BaseModel):
    prize: str
    user_id: int

    class Config:
        orm_mode: True


class careers(BaseModel):
    careers_name: str
    started_at: str
    ended_at: str
    user_id: int

    class Config:
        orm_mode: True


class leads(BaseModel):
    lead_name: str
    started_at: str
    ended_at: str
    user_id: int

    class Config:
        orm_mode: True


class projects(BaseModel):
    project_name: str
    project_img: str
    project_content: str
    user_id: int

    class Config:
        orm_mode: True


class certificate(BaseModel):
    certificate_name: str
    got_at: str
    user_id: int

    class Config:
        orm_mode: True


class skills(BaseModel):
    skill_name: str
    proficiency: int
    user_id: int

    class Config:
        orm_mode: True


class photos(BaseModel):
    href: str
    board_id: int

    class Config:
        orm_mode : True


class script(BaseModel):
    script_content : str
    author : str

    class Config:
        orm_mode : True

