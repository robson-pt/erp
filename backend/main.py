from fastapi import Depends, FastAPI

from .auth import fake_verify_token

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/products/")
def get_products():
    return [
        {"id": 1, "name": "Product A", "price": 10.99},
        {"id": 2, "name": "Product B", "price": 12.99},
        {"id": 3, "name": "Product C", "price": 15.99},
    ]


@app.get("/protegido")
def rota_protegida(token: str = Depends(fake_verify_token)):
    return {"data": "Área restrita!"}
