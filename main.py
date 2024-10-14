from fastapi import FastAPI, Form, Depends, HTTPException
from sqlalchemy import Date, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import date, datetime
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    birthDate = Column(Date)
    
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, birthDate: date, db: Session = Depends(get_db)):
    user = User(name=name, birthDate=birthDate)
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, birthDate: date, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.birthDate = birthDate
        db.commit()
        db.refresh(user)
        return user
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return None

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return None

@app.get("/users/checkage/{user_id}")
def check_user_age(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        today = datetime.now().date()
        age = today.year - user.birthDate.year - ((today.month, today.day) < (user.birthDate.month, user.birthDate.day))
        return {"id": user_id, "age": age, "is_over_18": age > 18}
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return None
    