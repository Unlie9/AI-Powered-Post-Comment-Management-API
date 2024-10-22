from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False, index=True)

    author_id = Column(Integer, ForeignKey("users.id"))

    author_post = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
