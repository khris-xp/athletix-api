class BookingHistory:
  def __init__(self) -> None:
    self.__bookings = []

  def get_bookings(self):
    return self.__bookings

  def get_booking_by_id(self, id: str) -> dict:
    for booking in self.__bookings:
      if booking.get_id() == id:
        return booking
    return None

  def get_bookings_by_user(self, id: str) -> list[dict]:
    return [booking for booking in self.__bookings if booking.get_customer()['id'] == id]

  def add_bookings(self, bookings: dict) -> dict:
    self.__bookings.append(bookings)
    return bookings
