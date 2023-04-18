from datetime import datetime
import uuid


class Person:
  def __init__(self, fullname: str, email: str, phone_number: str, address: str, birth_date: datetime, emergency_contact_fullname: str, emergency_contact_phone_number: str, account) -> None:
    self.__id = str(uuid.uuid4())
    self.__fullname = fullname
    self.__email = email
    self.__phone_number = phone_number
    self.__address = address
    self.__birth_date = birth_date
    self.__emergency_contact_fullname = emergency_contact_fullname
    self.__emergency_contact_phone_number = emergency_contact_phone_number
    self.__account = account

  def to_dict(self) -> dict:
    return {
        "id": self.get_id(),
        "fullname": self.get_fullname(),
        "email": self.get_email(),
        "phone_number": self.get_phone_number(),
        "address": self.get_address(),
        "birth_date": self.get_birth_date(),
        "emergency_contact_fullname": self.get_emergency_contact_fullname(),
        "emergency_contact_phone_number": self.get_emergency_contact_phone_number(),
        "account": self.get_account().to_dict()
    }

  def get_id(self) -> str:
    return self.__id

  def get_fullname(self) -> str:
    return self.__fullname

  def get_email(self) -> str:
    return self.__email

  def get_phone_number(self) -> str:
    return self.__phone_number

  def get_address(self) -> str:
    return self.__address

  def get_birth_date(self) -> datetime:
    return self.__birth_date

  def get_phone_number(self) -> str:
    return self.__phone_number

  def get_emergency_contact_fullname(self) -> str:
    return self.__emergency_contact_fullname

  def get_emergency_contact_phone_number(self) -> str:
    return self.__emergency_contact_phone_number

  def get_account(self):
    return self.__account

  def set_fullname(self, fullname: str) -> None:
    self.__fullname = fullname

  def set_email(self, email: str) -> None:
    self.__email = email

  def set_phone_number(self, phone_number: str) -> None:
    self.__phone_number = phone_number

  def set_address(self, address: str) -> None:
    self.__address = address

  def set_emergency_contact_fullname(self, emergency_contact_fullname: str) -> None:
    self.__emergency_contact_fullname = emergency_contact_fullname

  def set_emergency_contact_phone_number(self, emergency_contact_phone_number: str) -> None:
    self.__emergency_contact_phone_number = emergency_contact_phone_number
