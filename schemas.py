from pydantic import BaseModel
from typing import List, Optional

# User Schema
class UserBase(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str
    id: int

    class Config:
        orm_mode = True


# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str


# Blog Schema
class BlogBase(BaseModel):
    title: str
    content: str


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    title: str
    content: str
    id: int
    author_id: int
    comments: List["CommentResponse"] = []

    class Config:
        orm_mode = True


# Comment Schema
class CommentBase(BaseModel):
    content: str
    blog_id: int


class CommentCreate(BaseModel):
    content: str
    blog_id: int


class CommentResponse(BaseModel):
    id: int
    author_id: int
    content: str
    blog_id: int

    class Config:
        orm_mode = True
