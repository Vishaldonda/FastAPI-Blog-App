from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import engine, Base
from models import User, Blog, Comment
from schemas import UserCreate, Token, BlogCreate, BlogResponse, CommentCreate, CommentResponse
from utils import create_access_token, verify_password, get_password_hash
from dependencies import get_current_user, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    """
    Home route that greets the user or gives basic information about the API.
    """
    return {"message": "Welcome to the Blog API! Please use the available routes for user and blog operations."}

@app.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.delete("/delete_account", status_code=204)
def delete_account(password: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    # Verify the password
    if not verify_password(password, current_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )

    # Proceed with account deletion
    db.delete(current_user)
    db.commit()

    return {"message": "Account successfully deleted"}

@app.get("/blogs", response_model=list[BlogResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.post("/blogs/new", response_model=BlogCreate)
def create_new_blog(blog: BlogCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated, please login.")
    
    new_blog = Blog(title=blog.title, content=blog.content, author_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/blogs/{blog_id}", status_code=204)
def delete_blog(blog_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id, Blog.author_id == current_user.id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found or not authorized to delete")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}


@app.post("/comments", response_model=CommentResponse)
def add_comment(comment: CommentCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == comment.blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    new_comment = Comment(content=comment.content, blog_id=comment.blog_id, author_id=current_user.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@app.get("/comments/{blog_id}", response_model=list[CommentResponse])
def get_comments(blog_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.blog_id == blog_id).all()
    return comments


@app.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.author_id == current_user.id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found or not authorized to delete")
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}
