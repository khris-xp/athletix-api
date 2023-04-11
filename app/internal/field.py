import uuid


class Field:
  def __init__(self, name: str, description: str, price_by_slot: float, category: str, type: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__name = name
    self.__description = description
    self.__price_by_slot = price_by_slot
    self.__category = category
    self.__type = type
    self.__slots = []

  def get_id(self) -> str:
    return self.__id

  def get_name(self) -> str:
    return self.__name

  def get_description(self) -> str:
    return self.__description

  def get_price_by_slot(self) -> float:
    return self.__price_by_slot

  def get_category(self) -> str:
    return self.__category

  def get_type(self) -> str:
    return self.__type

  def get_slots(self) -> list:
    return self.__slots

  def set_name(self, name: str) -> None:
    self.__name = name

  def set_description(self, description: str) -> None:
    self.__description = description

  def set_price_by_slot(self, price_by_slot: float) -> None:
    self.__price_by_slot = price_by_slot

  def set_category(self, category: str) -> None:
    self.__category = category

  def set_type(self, type: str) -> None:
    self.__type = type

  def set_slots(self, slots: list) -> None:
    self.__slots = slots

  def add_slot(self, slot: dict) -> dict:
    self.__slots.append(slot)
    return slot
