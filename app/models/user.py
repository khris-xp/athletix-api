from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
  id: str
  fullname: str
  email: EmailStr
  phone_number: str
  address: str
  birth_date: str
  emergency_contact_fullname: str
  emergency_contact_phone_number: str
  account: dict
