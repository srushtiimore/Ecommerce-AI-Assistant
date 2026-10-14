from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import category_repository
from app.schemas.category import CategoryCreate, CategoryUpdate


def create_category(db: Session, category_data: CategoryCreate):
    return category_repository.create_category(db, category_data)


def get_categories(db: Session):
    return category_repository.get_categories(db)


def get_category(db: Session, category_id: int):
    category = category_repository.get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


def update_category(
    db: Session,
    category_id: int,
    category_data: CategoryUpdate
):
    category = category_repository.get_category_by_id(
        db,
        category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category_repository.update_category(
        db,
        category,
        category_data
    )


def delete_category(db: Session, category_id: int):
    category = category_repository.get_category_by_id(
        db,
        category_id
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    category_repository.delete_category(db, category)

    return {"message": "Category deleted successfully"}