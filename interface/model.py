from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base 

class info(Base):
    __tablename__ = "info"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(30))
    description = Column(String(255))
    github = Column(String(255))


class board(Base):
    __tablename__ = "board"
    board_id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(5000))
    created_at = Column(String(30))
    board_nickname = Column(String(255))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class comments(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    board_id = Column(Integer)
    created_at = Column(String(30))
    content = Column(String(255))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class contact(Base):
    __tablename__ = "contact"
    contact_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String(255))
    phone_number = Column(String(255))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class prizes(Base):
    __tablename__ = "prizes"
    prize_id = Column(Integer, primary_key=True, autoincrement=True)
    prize = Column(String(100))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class careers(Base):
    __tablename__ = "careers"
    careers_id = Column(Integer, primary_key=True, autoincrement=True)
    careers_name = Column(String(100))
    started_at = Column(String(30))
    ended_at = Column(String(30))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class leads(Base):
    __tablename__ = "leads"
    lead_id = Column(Integer, primary_key=True, autoincrement=True)
    lead_name = Column(String(100))
    started_at = Column(String(30))
    ended_at = Column(String(30))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class projects(Base):
    __tablename__ = "projects"
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(100))
    project_img = Column(String(255))
    project_content = Column(String(5000))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class certificate(Base):
    __tablename__ = "certificate"
    certificate_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_name = Column(String(255))
    got_at = Column(String(30))
    user_id = Column(Integer, ForeignKey("info.user_id"))


class skills(Base):
    __tablename__ = "skills"
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    skill_name = Column(String(255))
    proficiency = Column(Integer)
    user_id = Column(Integer, ForeignKey("info.user_id"))


class photos(Base):
    __tablename__ = "photos"
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    href = Column(String(255))
    board_id = Column(Integer, ForeignKey("board.board_id"))


class script(Base):
    __tablename__ = "script"
    script_id = Column(Integer, primary_key=True, autoincrement=True)
    script_content = Column(String(500))
    author = Column(String(100))

