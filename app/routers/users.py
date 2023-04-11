from fastapi import APIRouter, Depends
from ..utils.dependencies import get_current_user

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})


@router.get("/profile")
async def get_profile(current_user=Depends(get_current_user)):
  return current_user
