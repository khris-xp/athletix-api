from pydantic import BaseModel, EmailStr
from datetime import datetime


class AccountModel(BaseModel):
  full_name: str
  email: EmailStr
  password: str
  phone_number: str
  address: str
  birth_date: datetime
  emergency_contact_fullname: str
  emergency_contact_phone_number: str
