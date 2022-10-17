from pydantic import BaseModel


class info(BaseModel):
    user_id = int
    nickname = str
    blog = str
    github = str
