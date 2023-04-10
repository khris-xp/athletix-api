from .slot import Slot
from datetime import datetime


class SlotDate(Slot):
  def __init__(self, start_time: datetime, end_time: datetime, date: datetime) -> None:
    super().__init__(start_time, end_time)
    self.__date = date
    
  def get_date(self):
    return self.__date
  
  def set_date(self, date: datetime) -> None:
    self.__date = date