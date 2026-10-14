from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.order_item import (
    OrderItemCreate,
    OrderItemResponse,
    OrderItemUpdate,
)
from app.services import order_item_service


router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


@router.post(
    "",
    response_model=OrderItemResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order_item(
    item_data: OrderItemCreate,
    db: Session = Depends(get_db)
):
    return order_item_service.create_order_item(
        db,
        item_data
    )


@router.get(
    "",
    response_model=list[OrderItemResponse]
)
def get_order_items(
    db: Session = Depends(get_db)
):
    return order_item_service.get_order_items(db)


@router.get(
    "/{item_id}",
    response_model=OrderItemResponse
)
def get_order_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    return order_item_service.get_order_item(
        db,
        item_id
    )


@router.patch(
    "/{item_id}",
    response_model=OrderItemResponse
)
def update_order_item(
    item_id: int,
    item_data: OrderItemUpdate,
    db: Session = Depends(get_db)
):
    return order_item_service.update_order_item(
        db,
        item_id,
        item_data
    )


@router.delete("/{item_id}")
def delete_order_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    return order_item_service.delete_order_item(
        db,
        item_id
    )