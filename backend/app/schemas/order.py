from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    customer_id: int
    order_date: datetime | None = None
    status: str = "pending"
    total_amount: Decimal


class OrderUpdate(BaseModel):
    status: str | None = None
    total_amount: Decimal | None = None


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    order_date: datetime
    status: str
    total_amount: Decimal

    model_config = ConfigDict(from_attributes=True)