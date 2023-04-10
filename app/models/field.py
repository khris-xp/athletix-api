from pydantic import BaseModel
from ..models.slot import SlotModel


class FieldModel(BaseModel):
  name: str
  description: str
  price_by_slot: float
  category: str
  type: str
  slots: list[SlotModel]
