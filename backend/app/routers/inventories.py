from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.inventory import (
    InventoryCreate,
    InventoryResponse,
    InventoryUpdate
)
from app.services import inventory_service


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("",response_model=InventoryResponse,status_code=status.HTTP_201_CREATED)
def create_inventory(
    inventory_data: InventoryCreate,
    db: Session = Depends(get_db)
):
    return inventory_service.create_inventory(
        db,
        inventory_data
    )


@router.get("",response_model=list[InventoryResponse])
def get_inventories(db: Session = Depends(get_db)):
    return inventory_service.get_inventories(db)

@router.get("/low-stock", response_model=list[InventoryResponse])
def get_low_stock_items(db: Session = Depends(get_db)):
    return inventory_service.get_low_stock_items(db)

@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return inventory_service.get_inventory(
        db,
        inventory_id
    )


@router.get("/product/{product_id}",response_model=InventoryResponse)
def get_inventory_by_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return inventory_service.get_inventory_by_product(
        db,
        product_id
    )


@router.patch("/{inventory_id}",response_model=InventoryResponse)
def update_inventory(
    inventory_id: int,
    inventory_data: InventoryUpdate,
    db: Session = Depends(get_db)
):
    return inventory_service.update_inventory(
        db,
        inventory_id,
        inventory_data
    )


@router.delete("/{inventory_id}")
def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    return inventory_service.delete_inventory(
        db,
        inventory_id
    )