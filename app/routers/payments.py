from fastapi import APIRouter, Depends
from ..utils.dependencies import get_current_user
from ..models.payment import PaymentModel
from ..database.database import booking_history

router = APIRouter(prefix="/payments", tags=["payments"], responses={
                   404: {"description": "Not found"}})


@router.post("/pay")
async def create_payment(payment: PaymentModel, user=Depends(get_current_user)):
  
  # booking = 
  
  return {"message": "payment created"}
