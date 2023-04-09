from .person import Person
from datetime import datetime


class Customer(Person):
  def __init__(self, fullname: str, email: str, phone_number: str, address: str, birth_date: datetime, emergency_contact_fullname: str, emergency_contact_phone_number: str, account) -> None:
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number, account)