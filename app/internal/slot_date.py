from .slot import Slot
from datetime import datetime


class SlotDate(Slot):
  def __init__(self, start_time: datetime, end_time: datetime, date: datetime) -> None:
    super().__init__(start_time, end_time)
    self.__date = date

  def get_date(self):
    return self.__date
    
  def is_equal(self, start_time: datetime, end_time: datetime, date: datetime) -> bool:
    return self.__date == date and super().is_equal(start_time, end_time)
