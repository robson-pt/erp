# backend/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.database import Base

# Configuração do banco (SQLite para desenvolvimento)
# DATABASE_URL = "sqlite:///./erp.db"
# Para PostgreSQL
DATABASE_URL = "postgresql://user:password@localhost:5432/erp_db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
