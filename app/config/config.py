from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
  jwt_secret_key: str 
  algorithm: str 
  access_token_expire_minutes: int

  class Config:
    env_file = ".env"


@lru_cache()
def get_settings():
  return Settings()