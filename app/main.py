from auth.routers import router as users_routers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from order.routers import router as orders_routers
from products.routers import router as products_routers
from settings import ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_routers)
app.include_router(products_routers)
app.include_router(orders_routers)
