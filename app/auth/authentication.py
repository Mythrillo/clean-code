from auth.models import User
from auth.utils import Hash
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db: Session, email: str, password: str) -> bool | User:
    user = db.query(User).filter(User.email == email).first()
    if not user or not Hash.verify(password, user.hashed_password):
        return False
    return user
