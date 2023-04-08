from pydantic import BaseModel


class EquipmentModel(BaseModel):
  name: str
  price: float
  quantity: int
