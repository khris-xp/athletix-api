from .equipment import Equipment

class BasketBall(Equipment):
  def __init__(self, name: str, price: float, quantity: int) -> None:
    super().__init__(name, price, quantity)