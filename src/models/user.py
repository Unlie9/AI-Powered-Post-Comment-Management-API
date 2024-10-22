from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="author_post")
    comments = relationship("Comment", back_populates="author_comment")
