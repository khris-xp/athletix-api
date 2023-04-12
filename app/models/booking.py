from pydantic import BaseModel


class BookingModel(BaseModel):
  field_id: str
  start_time: str
  end_time: str
  date: str
  