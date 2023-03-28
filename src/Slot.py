class Slot:
  def __init__(self, start_time, end_time):
    self.__start_time = start_time
    self.__end_time = end_time
    self.__status = True

  def get_start_time(self):

    return self.__start_time

  def get_end_time(self):
    return self.__end_time

  def get_status(self):
    return self.__status

  def set_book(self):
    self.__status = False
    
  def cancel(self):
    self.__status = True
    
  def get_details(self):
    return {
        "start_time": self.get_start_time(),
        "end_time": self.get_end_time(),
        "status": self.get_status()
    }
    
class SlotDate(Slot):
  def __init__(self, start_time, end_time, date):
    super().__init__(start_time, end_time)
    self.__date = date

  def get_date(self):
    return self.__date

  def get_slot_date_details(self):
    return {
        "start_time": self.get_start_time(),
        "end_time": self.get_end_time(),
        "status": self.get_status(),
        "date": self.get_date()
    }


slot1 = SlotDate("10:00", "11:00", "2021-01-01")
slot2 = SlotDate("11:00", "12:00", "2021-01-01")
slot3 = SlotDate('12:00', '13:00', '2021-01-01')