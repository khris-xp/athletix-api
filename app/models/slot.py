from pydantic import BaseModel


class SlotDate(BaseModel):
  date: str
  start_time: str
  end_time: str
