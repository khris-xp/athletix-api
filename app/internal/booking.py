from datetime import datetime
import uuid


class Booking:
  def __init__(self, slot: dict, equipments: dict, customer_id: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__slot = slot
    self.__customer_id = customer_id
    self.__equipments = equipments
    self.__status = "Pending"
    self.__created_at = datetime.now()

  def get_id(self) -> str:
    return self.__id

  def get_slot(self) -> dict:
    return self.__slot

  def get_customer_id(self) -> str:
    return self.__customer_id

  def get_equipments(self) -> dict:
    return self.__equipments

  def get_status(self) -> str:
    return self.__status

  def set_status(self, status: str) -> None:
    self.__status = status
