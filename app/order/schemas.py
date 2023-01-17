from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    total: float
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class OrderWithNoUpdatedAt(OrderCreate):
    id: int
    created_at: datetime


class OrderGet(OrderWithNoUpdatedAt):
    updated_at: datetime | None


class OrderItemsBase(BaseModel):
    product_id: int
    order_id: int


class OrderItemsCreate(OrderItemsBase):
    amount: int

    class Config:
        orm_mode = True


class OrderItemsList(OrderItemsCreate):
    id: int


class OrderItemsJoinedWithProducts(BaseModel):
    amount: int
    order_id: int
    product_id: int
    price: float
    title: str


class OrderWithItems(BaseModel):
    order_id: int
    product_id: int
    amount: int
    total: float
    updated_at: datetime
