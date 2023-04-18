from .payment import Payment


class PromptPayPayment(Payment):
  def __init__(self, amount: float, is_payed=False) -> None:
    super().__init__(amount, is_payed)
    self.__slip_image = None
    
  def to_dict(self) -> dict:
    return {
      "id": self.get_id(),
      "amount": self.get_amount(),
      "is_payed": self.get_is_payed(),
      "slip_image": self.get_slip_image()
    }

  def set_slip_image(self, image: str) -> None:
    self.__slip_image = image

  def get_slip_image(self) -> str:
    return self.__slip_image