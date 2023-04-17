from pydantic import BaseModel

class CheckSlot(BaseModel):
  field_id: str
  date: str