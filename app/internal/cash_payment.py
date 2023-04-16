from .payment import Payment


class CashPayment(Payment):
  def __init__(self, amount: float, is_payed=False) -> None:
    super().__init__(amount, is_payed)
