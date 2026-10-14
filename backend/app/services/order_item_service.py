from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Inventory, Order, Product
from app.repositories import order_item_repository
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate


def create_order_item(db: Session, item_data: OrderItemCreate):
    order = db.query(Order).filter(
        Order.id == item_data.order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    product = db.query(Product).filter(
        Product.id == item_data.product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    inventory = db.query(Inventory).filter(
        Inventory.product_id == item_data.product_id
    ).first()

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found for this product"
        )

    if item_data.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )

    if item_data.quantity > inventory.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock. Available quantity: {inventory.quantity}"
        )

    unit_price = product.price
    subtotal = unit_price * item_data.quantity

    order_item = order_item_repository.create_order_item(
    db,
    item_data,
    unit_price,
    subtotal
)

    inventory.quantity -= item_data.quantity

    db.commit()
    db.refresh(inventory)

    return order_item


def get_order_items(db: Session):
    return order_item_repository.get_order_items(db)


def get_order_item(db: Session, item_id: int):
    order_item = order_item_repository.get_order_item_by_id(
        db,
        item_id
    )

    if not order_item:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    return order_item


def update_order_item(
    db: Session,
    item_id: int,
    item_data: OrderItemUpdate
):
    order_item = order_item_repository.get_order_item_by_id(
        db,
        item_id
    )

    if not order_item:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    return order_item_repository.update_order_item(
        db,
        order_item,
        item_data
    )


def delete_order_item(db: Session, item_id: int):
    order_item = order_item_repository.get_order_item_by_id(
        db,
        item_id
    )

    if not order_item:
        raise HTTPException(
            status_code=404,
            detail="Order item not found"
        )

    order_item_repository.delete_order_item(
        db,
        order_item
    )

    return {"message": "Order item deleted successfully"}