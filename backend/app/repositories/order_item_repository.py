from sqlalchemy.orm import Session

from app.database.models import OrderItem
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate


def create_order_item(
    db: Session,
    item_data: OrderItemCreate,
    unit_price,
    subtotal
):
    order_item = OrderItem(
        order_id=item_data.order_id,
        product_id=item_data.product_id,
        quantity=item_data.quantity,
        unit_price=unit_price,
        subtotal=subtotal
    )

    db.add(order_item)
    db.commit()
    db.refresh(order_item)

    return order_item


def get_order_items(db: Session):
    return db.query(OrderItem).all()


def get_order_item_by_id(db: Session, item_id: int):
    return (
        db.query(OrderItem)
        .filter(OrderItem.id == item_id)
        .first()
    )


def update_order_item(
    db: Session,
    order_item: OrderItem,
    item_data: OrderItemUpdate
):
    update_data = item_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(order_item, field, value)

    db.commit()
    db.refresh(order_item)

    return order_item


def delete_order_item(db: Session, order_item: OrderItem):
    db.delete(order_item)
    db.commit()