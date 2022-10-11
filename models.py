from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base


class info(Base):
    __tablename__ = "info"
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(255))
    blog = Column(String(255))
    github = Column(String(255))


class board(Base):
    __tablename__ = "board"
    board_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(5000))
    created_at = Column(DateTime)
    board_nickname = Column(String(255))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class photos(Base):
    __tablename__ = "photos"
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    href = Column(String(255))
    board_id = Column(Integer, ForeignKey("board.board_id"))
