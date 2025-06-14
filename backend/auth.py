from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_verify_token(token: str = Depends(oauth2_scheme)):
    if token != "senhasecreta":
        raise HTTPException(status_code=400, detail="Token inválido")
    return token
