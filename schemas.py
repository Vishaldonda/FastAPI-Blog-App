from pydantic import BaseModel
from typing import List, Optional

# Schemas
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

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Comments
class CommentBase(BaseModel):
    content: str
    blog_id: int

class CommentCreate(BaseModel):
    content: str
    blog_id: int

class CommentResponse(BaseModel):
    id: int
    content: str
    blog_id: int
    author_id: Optional[int]  # allow None for old data

    class Config:
        orm_mode = True

# Blogs
class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: Optional[int]  # allow None for old data
    comments: List[CommentResponse] = []  # default empty list

    class Config:
        orm_mode = True
