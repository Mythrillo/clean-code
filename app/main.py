from auth.routers import router as users_routers
from fastapi import FastAPI
from products.routers import router as products_routers

# from order.routers import router as orders_routers


app = FastAPI()

app.include_router(users_routers)
app.include_router(products_routers)
# app.include_router(orders_routers)
