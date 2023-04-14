import uuid


class Equipment:
  def __init__(self, name: str, price_per_unit: float, quantity: int) -> None:
    self.__id = str(uuid.uuid4())
    self.__name = name
    self.__price_per_unit = price_per_unit
    self.__quantity = quantity

  def get_id(self) -> str:
    return self.__id

  def get_name(self) -> str:
    return self.__name
  
  def get_quantity(self) -> int:
    return self.__quantity

  def get_price_per_unit(self) -> float:
    return self.__price_per_unit

  def set_quantity(self, quantity: int) -> None:
    self.__quantity = quantity

  def set_price_per_unit(self, price_per_unit: float) -> None:
    self.__price_per_unit = price_per_unit

  def set_name(self, name: str) -> None:
    self.__name = name
