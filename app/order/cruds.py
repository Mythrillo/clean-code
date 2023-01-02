from order import schemas
from order.models import Order, OrderItems
from sqlalchemy.orm import Session


def get_order(db: Session, order_id: int) -> Order:
    return db.query(Order).filter(Order.id == order_id).first()


def get_order_items(db: Session, order_id: int) -> list[OrderItems]:
    return db.query(OrderItems).filter(OrderItems.order_id == order_id).all()


def create_order(db: Session, order: schemas.OrderCreate) -> Order:
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    db.delete(order)
    db.commit()


def add_product_to_order(db: Session, order_item: schemas.OrderItemsCreate):
    db_order_item = create_order_item(db, order_item)
    order = get_order(db, db_order_item.order_id)

    # TODO: Update the total cost of order


def create_order_item(db: Session, order_item: schemas.OrderItemsCreate) -> OrderItems:
    db_order_item = OrderItems(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)

    return db_order_item
