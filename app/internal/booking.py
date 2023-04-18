from datetime import datetime
import uuid


class Booking:
  def __init__(self, slot: dict, equipments: dict, customer: dict, field: dict, payment: dict) -> None:
    self.__id = str(uuid.uuid4())
    self.__slot = slot
    self.__customer = customer
    self.__field = field
    self.__equipments = equipments
    self.__payment = payment
    self.__status = "pending"
    self.__created_at = datetime.now()

  def to_dict(self) -> dict:
    return {
        "id": self.get_id(),
        "slot": self.get_slot().to_dict(),
        "customer": self.get_customer(),
        "field": self.get_field(),
        "equipments": self.get_equipments(),
        "payment": self.get_payment().to_dict(),
        "status": self.get_status(),
        "created_at": self.get_created_at()
    }

  def get_id(self) -> str:
    return self.__id

  def get_slot(self) -> dict:
    return self.__slot

  def get_customer(self) -> str:
    return self.__customer

  def get_field(self) -> str:
    return self.__field

  def get_equipments(self) -> dict:
    return self.__equipments

  def get_status(self) -> str:
    return self.__status

  def get_payment(self) -> dict:
    return self.__payment

  def get_created_at(self) -> str:
    return self.__created_at

  def set_status(self, status: str) -> None:
    self.__status = status
