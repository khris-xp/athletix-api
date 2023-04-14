from pydantic import BaseModel


class BookingModel(BaseModel):
  field_id: str
  slot: dict
  equipments: list[dict]
  payment_method: str