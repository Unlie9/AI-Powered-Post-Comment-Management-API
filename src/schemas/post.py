from pydantic import BaseModel
from src.schemas.comment import Comment


class PostBase(BaseModel):
    text: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    author_id: int
    comments: list[Comment] = [] 

    class Config:
        orm_mode = True