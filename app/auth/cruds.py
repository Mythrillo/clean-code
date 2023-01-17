from auth import schemas
from auth.models import User
from sqlalchemy.orm import Session
from auth.authentication import get_password_hash


def get_user(db: Session, email: str) -> schemas.UserInDB:
    user = db.query(User).filter(User.email == email).first()
    return schemas.UserInDB(**user)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(email=user.email, hashed_password=get_password_hash(user.password), is_admin=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
