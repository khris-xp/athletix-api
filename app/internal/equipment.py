import uuid


class Equipment:
  def __init__(self, name: str, price: float, quantity: int) -> None:
    self.__id = str(uuid.uuid4())
    self.__name = name
    self.__price = price
    self.__quantity = quantity

  def get_id(self) -> str:
    return self.__id

  def get_name(self) -> str:
    return self.__name

  def set_quantity(self, quantity: int) -> None:
    self.__quantity = quantity

  def set_price(self, price: float) -> None:
    self.__price = price

  def set_name(self, name: str) -> None:
    self.__name = name
