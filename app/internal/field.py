from datetime import datetime
import uuid


class Field:
  def __init__(self, name: str, description: str, price_by_slot: float, category: str, type: str, image: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__name = name
    self.__description = description
    self.__price_by_slot = price_by_slot
    self.__category = category
    self.__type = type
    self.__image = image
    self.__booking_slots = []

  def to_dict(self) -> dict:
    return {
        "id": self.get_id(),
        "name": self.get_name(),
        "description": self.get_description(),
        "price_by_slot": self.get_price_by_slot(),
        "category": self.get_category(),
        "type": self.get_type(),
        "image": self.get_image(),
        "booking_slots": [slot.to_dict() for slot in self.get_booking_slots()],
    }

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

  def get_booking_slots(self) -> list:
    return self.__booking_slots

  def get_booking_slots_by_date(self, date: datetime) -> list[dict]:
    return [booking_slots for booking_slots in self.__booking_slots if booking_slots.get_date() == date]

  def get_image(self) -> str:
    return self.__image

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

  def set_booking_slots(self, booking_slots: list) -> None:
    self.__booking_slots = booking_slots

  def set_image(self, image: str) -> None:
    self.__image = image

  def add_slot(self, slot: dict) -> dict:
    return self.__booking_slots.append(slot) or slot
