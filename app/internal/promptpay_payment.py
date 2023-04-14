from .payment import Payment


class PromptPayPayment(Payment):
  def __init__(self, amount: float, is_payed=False) -> None:
    super().__init__(amount, is_payed)
    self.__slip_image = None

  def set_slip_image(self, image: str) -> None:
    self.__slip_image = image
