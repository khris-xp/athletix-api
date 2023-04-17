from pydantic import BaseModel


class EquipmentModel(BaseModel):
  name: str
  price_per_unit: float
  quantity: int
  category: str

class SearchEquipmentModel(BaseModel):
  category: str