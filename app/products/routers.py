from auth.routers import get_current_user
from auth.schemas import User
from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
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
async def delete_product(
    product_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    if current_user.is_admin:
        cruds.delete_product(db, product_id)
    else:
        raise HTTPException(status_code=403, detail="Not an admin user!")


@router.post("", response_model=schemas.ProductCreate)
async def create_product(
    product: schemas.ProductCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.is_admin:
        return cruds.create_product(db, product)
    else:
        raise HTTPException(status_code=403, detail="Not an admin user!")


@router.put("/{product_id}")
async def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if current_user.is_admin:
        return cruds.update_product(db, product_id, product)
    else:
        raise HTTPException(status_code=403, detail="Not an admin user!")
