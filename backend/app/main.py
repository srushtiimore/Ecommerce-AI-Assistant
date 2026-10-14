from fastapi import FastAPI

from app.routers.products import router as product_router
from app.routers.categories import router as category_router
from app.routers.customers import router as customer_router
from app.routers.inventories import router as inventory_router
from app.routers.orders import router as order_router
from app.routers.order_items import router as order_item_router



app = FastAPI(
    title="E-commerce AI Assistant",
    version="1.0.0"
)

app.include_router(product_router)
app.include_router(category_router)
app.include_router(customer_router)
app.include_router(inventory_router)
app.include_router(order_router)
app.include_router(order_item_router)



