from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_admin: bool

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    id: int
    is_admin: bool
    hashed_password: str


class TokenWithUserInfo(BaseModel):
    access_token: str
    token_type: str
    username: str
    email: str
    is_admin: bool


class TokenData(BaseModel):
    username: str | None = None
