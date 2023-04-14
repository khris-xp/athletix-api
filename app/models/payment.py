from pydantic import BaseModel


class PaymentModel(BaseModel):
  booking_id: str
  payment_id: str
  slip_image: str
