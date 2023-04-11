from pydantic import BaseModel
from datetime import datetime


class FieldModel(BaseModel):
  name: str
  description: str
  price_by_slot: float
  category: str
  type: str
