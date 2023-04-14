from datetime import datetime
import uuid


class Payment:
  def __init__(self, amount: float, is_payed=False) -> None:
    self.__id = str(uuid.uuid4())
    self.__amount = amount
    self.__is_payed = is_payed
    self.__created_at = datetime.now()

  def get_id(self) -> str:
    return self.__id

  def get_amount(self) -> float:
    return self.__amount

  def get_is_payed(self) -> bool:
    return self.__is_payed

  def set_is_payed(self, is_payed: bool) -> None:
    self.__is_payed = is_payed
