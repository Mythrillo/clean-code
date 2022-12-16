from fastapi import HTTPException, status
from products import schemas
from products.models import Product
from settings import MAX_GET_LIMIT
from sqlalchemy.orm import Session


def get_products(db: Session, offset: int = 0, limit: int = MAX_GET_LIMIT) -> list[Product]:
    return list(db.query(Product).filter().offset(offset).limit(limit))


def create_product(db: Session, product: schemas.ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: int) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate) -> Product:
    db.query(Product).filter(Product.id == product_id).update(product.dict(), synchronize_session="fetch")
    db.commit()
    return product
