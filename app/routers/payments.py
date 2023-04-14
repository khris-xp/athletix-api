from fastapi import APIRouter, Depends
from ..utils.dependencies import get_current_user
from ..models.payment import PromptpayPaymentModel
from ..database.database import booking_history

router = APIRouter(prefix="/payments", tags=["payments"], responses={
                   404: {"description": "Not found"}})


@router.post("/pay/promptpay")
async def pay_promptpay(payment: PromptpayPaymentModel, user=Depends(get_current_user)):
  return {"message": "Promptpay Payment"}
  