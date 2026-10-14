from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import order_repository
from app.schemas.order import OrderCreate, OrderUpdate


def create_order(db: Session, order_data: OrderCreate):
    return order_repository.create_order(db, order_data)


def get_orders(db: Session):
    return order_repository.get_orders(db)


def get_order(db: Session, order_id: int):
    order = order_repository.get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


def update_order(
    db: Session,
    order_id: int,
    order_data: OrderUpdate
):
    order = order_repository.get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order_repository.update_order(
        db,
        order,
        order_data
    )


def delete_order(db: Session, order_id: int):
    order = order_repository.get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order_repository.delete_order(db, order)

    return {"message": "Order deleted successfully"}