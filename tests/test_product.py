import pytest

from backend.db import SessionLocal
from backend.models.product import Product


@pytest.fixture
def db_session():
    from backend.db import Base, engine

    Base.metadata.create_all(engine)
    db = SessionLocal()
    yield db
    db.rollback()
    db.close()


def test_product_creation(db_session):
    product = Product(name="Notebook", quantity=5, price=250000)
    db_session.add(product)
    db_session.commit()

    saved_product = db_session.query(Product).first()
    assert saved_product.name == "Notebook"
    assert saved_product.price == 250000  # R$ 2.500,00
