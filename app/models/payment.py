from pydantic import BaseModel


class PromptpayPaymentModel(BaseModel):
  booking_id: str
  slip_image: str


class CashPaymentModel(BaseModel):
  booking_id: str
  cash: float
