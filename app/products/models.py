from db import Base
from sqlalchemy import Column, Float, Integer, String


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, unique=True)
    description = Column(String(255))
    price = Column(Float)
