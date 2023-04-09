from fastapi import APIRouter, HTTPException, status
from ..internal.customer import Customer
from ..internal.account import Account
from ..database import stadium
from ..models.account import AccountModel

router = APIRouter(prefix='/auth', tags=['auth'], responses={
                   404: {'description': 'Not found'}})


@router.post('/register')
async def register(body: AccountModel):
  if stadium.get_user_by_email(body.email) is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Email already exists')

  if stadium.get_user_by_fullname(body.fullname) is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Fullname already exists')

  if stadium.get_user_by_phone_number(body.phone_number) is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Phone number already exists')

  account = Account(password=body.password)

  person = Customer(fullname=body.fullname, email=body.email, phone_number=body.phone_number, address=body.address, birth_date=body.birth_date,
                    emergency_contact_fullname=body.emergency_contact_fullname, emergency_contact_phone_number=body.emergency_contact_phone_number, account=account)

  new_person = stadium.add_user(person)

  return new_person


@router.post('/login')
async def login():
  return {'message': 'Login a user'}
