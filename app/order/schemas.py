from pydantic import BaseModel


class OrderBase(BaseModel):
    owner_id: int


class OrderCreate(OrderBase):
    total: float

    class Config:
        orm_mode = True


class OrderItemsBase(BaseModel):
    product_id: int
    order_id: int


class OrderItemsCreate(OrderItemsBase):
    amount: int

    class Config:
        orm_mode = True
