class Slot:
  def __init__(self, created_on, start_time, end_time):
    self.__created_on = created_on
    self.__start_time = start_time
    self.__end_time = end_time


class SlotDate(Slot):
  def __init__(self, created_on, start_time, end_time, date):
    super().__init__(created_on, start_time, end_time)
    self.__date = date
    
slot1 = SlotDate("2021-01-01", "10:00", "11:00", "2021-01-01")
slot2 = SlotDate("2021-01-01", "11:00", "12:00", "2021-01-01")