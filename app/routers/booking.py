from fastapi import APIRouter, Depends
from ..utils.dependencies import get_current_user

router = APIRouter(prefix="/booking",
                   tags=["booking"], responses={404: {"description": "Not found"}})


@router.post("/")
async def create_booking(current_user=Depends(get_current_user)):
  return {"message": "Book a new appointment"}


@router.get("/history")
async def get_history(current_user=Depends(get_current_user)):
  return {"message": "Get booking history"}


@router.post("/cancel")
async def cancel_booking(current_user=Depends(get_current_user)):
  return {"message": "Cancel an appointment"}
