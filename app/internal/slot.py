from datetime import datetime
import uuid


class Slot:
  def __init__(self, start_time: datetime, end_time: datetime) -> None:
    self.__id = str(uuid.uuid4())
    self.__start_time = start_time
    self.__end_time = end_time
    self.__is_booked = False

  def to_dict(self) -> dict:
    return {
        key.replace("_Slot__", ""): value
        for key, value in self.__dict__.items()
    }

  def get_id(self) -> str:
    return self.__id

  def get_start_time(self) -> datetime:
    return self.__start_time

  def get_end_time(self) -> datetime:
    return self.__end_time

  def get_is_booked(self) -> bool:
    return self.__is_booked

  def set_is_booked(self, is_booked: bool) -> None:
    self.__is_booked = is_booked
