from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import time

security = HTTPBearer()

SECRET = "97791d4db2aa5f689c3cc39356ce35762f0a73aa70923039d8ef72a2840a1b02"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])

        if payload["exp"] < int(time.time()):
            raise HTTPException(status_code=401, detail="Token expired")

        return payload

    except:
        raise HTTPException(status_code=401, detail="Invalid token")