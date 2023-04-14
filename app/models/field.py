from pydantic import BaseModel


class FieldModel(BaseModel):
  name: str
  description: str
  price_by_slot: float
  category: str
  type: str
