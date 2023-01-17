import jwt
import settings
from auth import cruds, schemas
from auth.authentication import authenticate_user, CredentialsException, create_access_token
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError
from datetime import timedelta

router = APIRouter(tags=["Accounts"], prefix="/accounts")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise CredentialsException()
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return schemas.Token(access_token=access_token, token_type="bearer")


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


@router.get("/user/me", response_model=schemas.User)
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CredentialsException()
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise CredentialsException()
    user = cruds.get_user(db, email=token_data.email)
    if user is None:
        raise CredentialsException()
    return user


@router.get(
    "/user/{email}",
    response_model=schemas.User,
)
async def get_user_by_email(
    email: str, current_user: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)
):
    user = cruds.get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User doesn't exist")
    if not current_user.is_admin and user.email != email:
        raise HTTPException(status_code=403, detail="Can't access that information")
    return user
