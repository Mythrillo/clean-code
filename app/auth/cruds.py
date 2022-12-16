from auth import schemas
from auth.models import User
from auth.utils import Hash
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password, is_admin=False)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
