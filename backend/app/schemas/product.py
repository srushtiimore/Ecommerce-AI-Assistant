from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    category_id: int
    name: str
    description: str | None = None
    price: Decimal


class ProductUpdate(BaseModel):
    category_id: int | None = None
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None


class ProductResponse(BaseModel):
    id: int
    category_id: int
    name: str
    description: str | None
    price: Decimal

    model_config = ConfigDict(from_attributes=True) #from_attributes=True allows our Pydantic response schema to read data from SQLAlchemy model objects.