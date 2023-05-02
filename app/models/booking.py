from pydantic import BaseModel


class BookingModel(BaseModel):
  field_id: str
  slot: dict
  equipments: list[dict]
  payment_method: str


class ApproveBookingModel(BaseModel):
  booking_id: str
  
class CancelBookingModel(BaseModel):
  booking_id: str