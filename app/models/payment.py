from pydantic import BaseModel


class PromptpayPaymentModel(BaseModel):
  booking_id: str
  payment_id: str
  slip_image: str
