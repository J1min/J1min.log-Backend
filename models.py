from sqlalchemy import Column, Integer, String
from database import Base


class info(Base):
    __tablename__ = "info"
    user_id = Column(Integer, primary_key=True)
    nickname = Column(String(20))
    blog = Column(String(200))
    github = Column(String(200))
