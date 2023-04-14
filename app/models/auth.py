from pydantic import BaseModel, EmailStr


class RegisterModel(BaseModel):
  fullname: str
  email: EmailStr
  password: str
  phone_number: str
  address: str
  birth_date: str
  emergency_contact_fullname: str
  emergency_contact_phone_number: str


class LoginModel(BaseModel):
  email: EmailStr
  password: str

class ChangePasswordModel(BaseModel):
  old_password: str
  new_password: str