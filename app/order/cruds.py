from fastapi import HTTPException, status
from order import schemas
from order.models import Order, OrderItems
from products.cruds import get_product
from products.models import Product
from sqlalchemy.orm import Session


def get_order(db: Session, order_id: int, user_id: int) -> Order:
    order = db.query(Order).filter(Order.id == order_id, Order.owner_id == user_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


def get_order_items(db: Session, order_id: int, user_id: int) -> list[OrderItems]:
    get_order(db, order_id, user_id)
    return (
        db.query(OrderItems.amount, OrderItems.order_id, Product.id.label("product_id"), Product.title, Product.price)
        .join(Product)
        .filter(OrderItems.order_id == order_id)
        .all()
    )


def create_order(db: Session, owner_id: int) -> Order:
    db_order = Order(owner_id=owner_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int, user_id: int):
    order = get_order(db, order_id, user_id)
    _delete_order_items(db, order_id)
    db.delete(order)
    db.commit()


def _delete_order_items(db: Session, order_id: int):
    order_items = db.query(OrderItems).filter(OrderItems.order_id == order_id).all()
    for order_item in order_items:
        db.delete(order_item)
    db.commit()


def add_product_to_order(db: Session, order_item: schemas.OrderItemsCreate, user_id: int):
    order = get_order(db, order_item.order_id, user_id)
    db_order_item = _create_or_update_order_item(db, order_item)

    product = get_product(db, db_order_item.product_id)
    order.total += product.price * order_item.amount
    _update_order(db, schemas.OrderWithNoUpdatedAt(**order.__dict__))
    return schemas.OrderWithItems(
        order_id=order.id,
        amount=db_order_item.amount,
        product_id=db_order_item.product_id,
        total=order.total,
        updated_at=order.updated_at,
    )


def _create_or_update_order_item(db: Session, order_item: schemas.OrderItemsCreate) -> OrderItems:
    db_order_item = (
        db.query(OrderItems)
        .filter(OrderItems.order_id == order_item.order_id, OrderItems.product_id == order_item.product_id)
        .first()
    )
    if not db_order_item:
        db_order_item = OrderItems(**order_item.dict())
        db.add(db_order_item)
    else:
        print("Already exists")
        print(db_order_item)
        amount = order_item.amount + db_order_item.amount
        db.query(OrderItems).filter(
            OrderItems.order_id == order_item.order_id, OrderItems.product_id == order_item.product_id
        ).update({"amount": amount})
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


def _update_order(db: Session, order: schemas.OrderGet):
    db.query(Order).filter(Order.id == order.id).update(order.dict(), synchronize_session="fetch")
    db.commit()


def list_orders(db: Session, user_id: int) -> list[Order]:
    return db.query(Order).filter(Order.owner_id == user_id).all()
