from db import get_db
from fastapi import APIRouter, Depends, status
from products import cruds, schemas
from sqlalchemy.orm import Session

router = APIRouter(tags=["Products"], prefix="/products")


@router.get("/list", response_model=list[schemas.ProductList])
async def list_products(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return cruds.get_products(db, offset=offset, limit=limit)


@router.get("/{product_id}", response_model=schemas.ProductList)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    return cruds.get_product(db, product_id)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    cruds.delete_product(db, product_id)


@router.post("", response_model=schemas.ProductCreate)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return cruds.create_product(db, product)


@router.put("/{product_id}")
async def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return cruds.update_product(db, product_id, product)
