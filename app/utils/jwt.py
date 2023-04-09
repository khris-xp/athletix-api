from jose import jwt
from datetime import datetime, timedelta
from ..config.config import settings


def create_access_token(data: dict):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(
      to_encode, settings.jwt_secret_key, algorithm=settings.algorithm)
  return encoded_jwt
