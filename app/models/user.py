from pydantic import BaseModel


class UserModel(BaseModel):
  id: str
  fullname: str
  email: str
  phone_number: str
  address: str
  birth_date: str
  emergency_contact_fullname: str
  emergency_contact_phone_number: str
  account: dict
