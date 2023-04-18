class BookingHistory:
  def __init__(self) -> None:
    self.__bookings = []

  def get_bookings(self):
    return self.__bookings
  
  def get_booking_by_id(self, id: str) -> dict:
    return next((booking for booking in self.__bookings if booking.get_id() == id), None)

  def get_bookings_by_user(self, id: str) -> list[dict]:
    return [booking for booking in self.__bookings if booking.get_customer()['id'] == id]

  def add_bookings(self, bookings: dict) -> dict:
    return self.__bookings.append(bookings) or bookings
