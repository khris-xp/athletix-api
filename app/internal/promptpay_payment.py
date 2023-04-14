from .payment import Payment


class PromptPayPayment(Payment):
  def __init__(self, amount: float, is_payed: bool) -> None:
    super().__init__(amount, is_payed)
