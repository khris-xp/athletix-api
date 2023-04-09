from fastapi import APIRouter
from ..dependencies import get_current_user
from fastapi import Depends
from ..models.user import UserModel
from ..database import stadium

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})


@router.get("/profile", response_model=UserModel)
async def get_profile(current_user = Depends(get_current_user)):
  return current_user

@router.get("/")
async def get_users():
  return stadium.get_users()