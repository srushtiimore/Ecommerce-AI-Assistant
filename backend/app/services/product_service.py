from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import product_repository
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, product_data: ProductCreate):
    return product_repository.create_product(db, product_data)


def get_products(db: Session):
    return product_repository.get_products(db)


def get_product(db: Session, product_id: int):
    product = product_repository.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):
    product = product_repository.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product_repository.update_product(
        db,
        product,
        product_data
    )


def delete_product(db: Session, product_id: int):
    product = product_repository.get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product_repository.delete_product(db, product)

    return {"message": "Product deleted successfully"}