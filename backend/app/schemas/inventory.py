from pydantic import BaseModel, ConfigDict


class InventoryCreate(BaseModel):
    product_id: int
    quantity: int = 0
    reorder_level: int = 10


class InventoryUpdate(BaseModel):
    quantity: int | None = None
    reorder_level: int | None = None


class InventoryResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    reorder_level: int

    model_config = ConfigDict(from_attributes=True)