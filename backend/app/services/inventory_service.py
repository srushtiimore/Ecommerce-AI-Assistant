from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import inventory_repository
from app.schemas.inventory import InventoryCreate, InventoryUpdate


def create_inventory(
    db: Session,
    inventory_data: InventoryCreate
):
    return inventory_repository.create_inventory(
        db,
        inventory_data
    )


def get_inventories(db: Session):
    return inventory_repository.get_inventories(db)


def get_inventory(
    db: Session,
    inventory_id: int
):
    inventory = inventory_repository.get_inventory_by_id(
        db,
        inventory_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    return inventory


def get_inventory_by_product(
    db: Session,
    product_id: int
):
    inventory = inventory_repository.get_inventory_by_product_id(
        db,
        product_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found for this product"
        )

    return inventory


def update_inventory(
    db: Session,
    inventory_id: int,
    inventory_data: InventoryUpdate
):
    inventory = inventory_repository.get_inventory_by_id(
        db,
        inventory_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    return inventory_repository.update_inventory(
        db,
        inventory,
        inventory_data
    )


def delete_inventory(
    db: Session,
    inventory_id: int
):
    inventory = inventory_repository.get_inventory_by_id(
        db,
        inventory_id
    )

    if not inventory:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    inventory_repository.delete_inventory(
        db,
        inventory
    )

    return {"message": "Inventory deleted successfully"}

def get_low_stock_items(db: Session):
    return inventory_repository.get_low_stock_items(db)