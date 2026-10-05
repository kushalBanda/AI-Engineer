from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import Annotated
import secrets

import models
from database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Security Scheme: OAuth2 with Bearer Token
# This tells FastAPI that the URL to get a token is "/token"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password Hashing
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Dependency to verify the Token
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    # 1. Look for the token in the database
    db_token = db.query(models.Token).filter(models.Token.access_token == token).first()
    
    if not db_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Return the user associated with that token
    return db_token.user

@app.post("/users/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(password)
    new_user = models.User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"username": new_user.username, "msg": "User created"}

@app.post("/token")
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    # 1. Find the user
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Create a random token (Opaque Token)
    access_token = secrets.token_urlsafe(32)
    
    # 3. Save the token to the database
    db_token = models.Token(access_token=access_token, user_id=user.id)
    db.add(db_token)
    db.commit()
    
    # 4. Return the token
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
def read_current_user(user: Annotated[models.User, Depends(get_current_user)]):
    return {"username": user.username, "id": user.id, "auth_type": "Bearer Token (Opaque)"}