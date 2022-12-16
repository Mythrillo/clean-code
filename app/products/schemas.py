from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: str
    price: float


class ProductCreate(ProductBase):
    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    description: str
    price: float

    class Config:
        orm_mode = True


class ProductList(ProductBase):
    id: int

    class Config:
        orm_mode = True
