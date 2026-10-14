from sqlalchemy.orm import Session

from app.database.models import Order
from app.schemas.order import OrderCreate, OrderUpdate


def create_order(db: Session, order_data: OrderCreate):
    order = Order(**order_data.model_dump(exclude_none=True))

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_orders(db: Session):
    return db.query(Order).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def update_order(
    db: Session,
    order: Order,
    order_data: OrderUpdate
):
    update_data = order_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(order, field, value)

    db.commit()
    db.refresh(order)

    return order


def delete_order(db: Session, order: Order):
    db.delete(order)
    db.commit()