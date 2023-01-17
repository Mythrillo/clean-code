from auth import schemas
from auth.authentication import get_password_hash
from auth.models import User
from sqlalchemy.orm import Session


def get_user(db: Session, username: str) -> schemas.UserInDB:
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        return None
    db_user = schemas.UserInDB(**user.__dict__)
    return db_user


def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_admin=False,
        username=user.username,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
