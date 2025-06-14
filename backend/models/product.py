from sqlalchemy import Column, Integer, String

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer, default=0)

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
