from pydantic import BaseModel


class SlotModel(BaseModel):
  start_time: str
  end_time: str
  date: str
