from fastapi import APIRouter, Depends, HTTPException, status
from ..utils.dependencies import get_current_user
from ..models.payment import PromptpayPaymentModel, CashPaymentModel
from ..database.database import booking_history

router = APIRouter(prefix="/payments", tags=["payments"], responses={
                   404: {"description": "Not found"}})


@router.post("/pay/promptpay")
async def pay_promptpay(payment: PromptpayPaymentModel, user=Depends(get_current_user)):
  booking_exist = booking_history.get_booking_by_id(payment.booking_id)

  if booking_exist is None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Booking not found")

  booking_exist.get_payment().set_slip_image(payment.slip_image)
  
  booking_exist.get_payment().set_is_payed(True) 

  return {"message": "Create payment successfully"}


@router.post("/pay/cash")
async def pay_cash(payment: CashPaymentModel, user=Depends(get_current_user)):
  booking_exist = booking_history.get_booking_by_id(payment.booking_id)

  if booking_exist is None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Booking not found")

  if payment.cash < booking_exist.get_payment().get_amount():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Cash not enough")

  booking_exist.get_payment().set_is_payed(True)

  return {"message": "Create payment successfully"}
