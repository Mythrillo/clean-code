import jwt
import settings
from auth import cruds, schemas
from auth.authentication import authenticate_user
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["Accounts"], prefix="/accounts")


@router.post(
    "/token",
)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    user = {"id": user.id, "email": user.email, "is_admin": user.is_admin}
    token = jwt.encode(user, settings.JWT_SECRET)
    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/user/",
    response_model=schemas.User,
)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = cruds.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = cruds.create_user(db=db, user=user)
    return user


@router.get(
    "/user/{id}",
    response_model=schemas.User,
)
async def get_user_by(id: int, db: Session = Depends(get_db)):
    user = cruds.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    return user
