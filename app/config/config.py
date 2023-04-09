from pydantic import BaseSettings


class Settings(BaseSettings):
  jwt_secret_key: str = "secret"
  algorithm: str = "HS256"
  access_token_expire_minutes: int = 1440


settings = Settings()
