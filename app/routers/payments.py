from fastapi import APIRouter, Depends
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/payments", tags=["payments"], responses={
                   404: {"description": "Not found"}})


@router.post("/")
async def create_payment(current_user=Depends(get_current_user)):
  return {"message": "payment created"}


@router.post("/cancel")
async def cancel_payment(current_user=Depends(get_current_user)):
  return {"message": "payment cancelled"}
