from auth.routers import get_current_user
from auth.schemas import User
from db import get_db
from fastapi import APIRouter, Depends, status
from order import cruds, schemas
from sqlalchemy.orm import Session

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post("", response_model=schemas.OrderCreate)
async def create_order(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return cruds.create_order(db, current_user.id)


@router.get("/current", response_model=schemas.OrderGet)
async def get_current_order(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return cruds.get_current_order(db, current_user.id)


@router.post("/current")
async def mark_current_order_as_finished(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    cruds.finish_current_order(db, current_user.id)


@router.get("/{order_id}", response_model=schemas.OrderGet)
async def get_order(order_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return cruds.get_order(db, order_id, current_user.id)


@router.post("/add_product", response_model=schemas.OrderWithItems)
async def add_product_to_order(
    order_item: schemas.OrderItemsCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return cruds.add_product_to_order(db, order_item, current_user.id)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    cruds.delete_order(db, order_id, current_user.id)


@router.get("/{order_id}/products", response_model=list[schemas.OrderItemsJoinedWithProducts])
async def get_order_products(
    order_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return cruds.get_order_items(db, order_id, current_user.id)


@router.get("", response_model=list[schemas.OrderGet])
async def list_orders(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return cruds.list_orders(db, current_user.id)
