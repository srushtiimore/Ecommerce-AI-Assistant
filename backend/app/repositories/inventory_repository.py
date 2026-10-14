from sqlalchemy.orm import Session

from app.database.models import Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate


def create_inventory(db: Session, inventory_data: InventoryCreate):
    inventory = Inventory(**inventory_data.model_dump())

    db.add(inventory)
    db.commit()
    db.refresh(inventory)

    return inventory


def get_inventories(db: Session):
    return db.query(Inventory).all()


def get_inventory_by_id(db: Session, inventory_id: int):
    return (
        db.query(Inventory)
        .filter(Inventory.id == inventory_id)
        .first()
    )


def get_inventory_by_product_id(db: Session, product_id: int):
    return (
        db.query(Inventory)
        .filter(Inventory.product_id == product_id)
        .first()
    )


def update_inventory(
    db: Session,
    inventory: Inventory,
    inventory_data: InventoryUpdate
):
    update_data = inventory_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(inventory, field, value)

    db.commit()
    db.refresh(inventory)

    return inventory


def delete_inventory(db: Session, inventory: Inventory):
    db.delete(inventory)
    db.commit()

def get_low_stock_items(db: Session):
    return (
        db.query(Inventory)
        .filter(Inventory.quantity <= Inventory.reorder_level)
        .all()
    )    