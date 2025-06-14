from sqlalchemy import Column, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Integer)  # Em centavos para evitar problemas com float
