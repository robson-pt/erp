# backend/init_db.py
from .db import init_db

if __name__ == "__main__":
    init_db()
    print("✅ Banco de dados inicializado!")
