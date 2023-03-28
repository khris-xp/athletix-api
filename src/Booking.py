from src.Stadium import stadium
import uuid
from datetime import datetime
from src.Payment import Payment

class Booking:
    def __init__(self,description,slot, customer,equipment,status="Pending", created_on=datetime.now(), booking_id=uuid.uuid1()):
        self.__booking_id = booking_id
        self.__status = status
        self.__created_on = created_on
        self.__description = description
        self.__equipment = equipment
        self.__customer = customer
        self.__slot = slot
        
 
    
    def approve(self):
        self.__status = 'Approved'
        self.__slot.get_book()
    
    def cancel(self):
        self.__status = 'Cancel'
        self.__slot.cancel()
        
    def get_booking_id(self):
        return self.__booking_id
        
    def get_customer(self):
        return self.__customer

    def create_payment(self):
        pass

    def get_booking_detail(self):
        return {
            "booking_id": self.get_booking_id(),
            "status": self.__status,
            "created_on": self.__created_on,
            "description": self.__description,
            "equipment": self.__equipment,
            "customer": self.__customer,
        }

    

class BookingHistory:
    def __init__(self):
        self.__booking = []

    def search_booking_by_id(self):
        pass
    
    def create_booking(self,description, slot, customer,equipment):
        book = Booking(description, slot, customer,equipment)
        self.__booking.append(book)
        return book.get_booking_detail()
    
    def show_booking_history(self):
        to_return = []
        for book in self.__booking:
            print(book.get_booking_detail())
            to_return.append(book)
        return to_return
    
    def show_booking_by_id(self, booking_id):
        for book in self.__booking:
            if book.get_booking_id() == booking_id:
                return book.get_booking_detail()
        return "Not Found Booking"
        

class Equipment:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__status = "available"
        
    def get_book(self):
        self.__status = "booked"
    def return_book(self):
        self.__status = "available"
    def get_status(self):
        return self.__status
    
    def get_details(self):
        return {
            "name": self.__name,
            "price": self.__price,
            "status": self.__status
        }


class Vest(Equipment):
    def __init__(self, name):
        super().__init__(name, price=15)


class Football(Equipment):
    def __init__(self, name):
        super().__init__(name, price=50)



ball1 = Football('Ball 1')
ball2 = Football('Ball 2')
ball3 = Football('Ball 3')
ball4 = Football('Ball 4')
ball5 = Football('Ball 5')

vest1 = Vest('Vest 1')
vest2 = Vest('Vest 2')
vest3 = Vest('Vest 3')
vest4 = Vest('Vest 4')