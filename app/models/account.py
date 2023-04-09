from pydantic import BaseModel, EmailStr


class AccountModel(BaseModel):
  fullname: str
  email: EmailStr
  password: str
  phone_number: str
  address: str
  birth_date: str
  emergency_contact_fullname: str
  emergency_contact_phone_number: str
