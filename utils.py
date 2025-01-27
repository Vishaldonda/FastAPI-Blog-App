from datetime import datetime, timedelta
from jose import jwt
import bcrypt

SECRET_KEY = "fee104a9e7ce7f80363ce1ea0a37a229d61f169136422a656a08ec447dacf422"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_password_hash(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')  

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
