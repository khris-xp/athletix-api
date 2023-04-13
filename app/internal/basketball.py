from .equipment import Equipment

class BasketBall(Equipment):
  def __init__(self, name: str, price_per_unit: float, quantity: int) -> None:
    super().__init__(name, price_per_unit, quantity)