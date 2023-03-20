class Booking:
    def __init__(self, booking_id, status, created_on, description):
        self._booking_id = booking_id
        self._status = status
        self._created_on = created_on
        self._description = description
        self._equipment = Equipment

    def cancel(self):
        pass

    def create_payment(self):
        pass

    def set_equipment(self):
        pass

    def get_booking_card(self):
        pass

    def add_booking(self, booking_history):
        booking_history.booking.append(self)


class BookingHistory:
    def __init__(self):
        self.booking = []

    def search_booking_by_id(self):
        pass


class Equipment:
    def __init__(self, name, price, item):
        self._name = name
        self._price = price
        self._item = item


class Vest(Equipment):
    def __init__(self, name, price, item):
        super().__init__(name, price, item)


class Football(Equipment):
    def __init__(self, name, price, item):
        super().__init__(name, price, item)


# Instance
booking1 = Booking(1, True, '21/2/2023', 'Football')
booking2 = Booking(2, True, '20/3/2023', 'Basketball')

booking_history = BookingHistory()
booking1.add_booking(booking_history)

equipment1 = Football('Ball 1', 210, 10)
equipment2 = Football('Ball 2', 100, 20)
equipment3 = Vest('Vest 1', 200, 10)
equipment4 = Vest('Vest 2', 150, 10)
