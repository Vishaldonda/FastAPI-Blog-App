from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    blogs = relationship("Blog", back_populates="author")  
    comments = relationship("Comment", back_populates="owner")


class Blog(Base):
    __tablename__ = "blogs"  

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="blogs")  
    comments = relationship("Comment", back_populates="blog")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    blog_id = Column(Integer, ForeignKey("blogs.id"))  
    author_id = Column(Integer, ForeignKey("users.id"))
    blog = relationship("Blog", back_populates="comments")  
    owner = relationship("User", back_populates="comments")
