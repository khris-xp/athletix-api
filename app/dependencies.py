from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config.config import get_settings
from pydantic import BaseModel
from .database import stadium
from functools import wraps

settings = get_settings()


class TokenData(BaseModel):
  id: str
  role: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
  return pwd_context.hash(password)


def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(
      to_encode, settings.jwt_secret_key, algorithm=settings.algorithm)
  return encoded_jwt


def authenticate_user(email, password):
  user = stadium.get_user_by_email(email)
  if not user:
    return None
  if not verify_password(password, user.get_account().get_password()):
    return None
  return user


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={
          "WWW-Authenticate": "Bearer"
      })

  try:
    payload = jwt.decode(token, settings.jwt_secret_key,
                         algorithms=[settings.algorithm])
    user_id: str = payload.get("sub")
    role: str = payload.get("role")
    if user_id is None or role is None:
      raise credentials_exception

    token_data = TokenData(id=user_id, role=role)

  except JWTError:
    raise credentials_exception

  user = stadium.get_user_by_id(user_id)
  if user is None:
    raise credentials_exception
  return user


def role_required(role: str):
  def decorator(func):
    @wraps(func)
    async def wrapper(*args, user=Depends(get_current_user), **kwargs):
      if user.get_account().get_role() != role:
        raise HTTPException(status_code=403, detail="Forbidden")

      return await func(*args, user=user, **kwargs)

    return wrapper
  return decorator
