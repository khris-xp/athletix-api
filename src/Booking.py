from src.Stadium import stadium
import uuid
from datetime import datetime
from src.Payment import Payment,QRCodeTransaction,CashTransaction

class Booking:
    def __init__(self,description,slot, customer,equipment,status="Pending", created_on=datetime.now(), booking_id=uuid.uuid1()):
        self.__booking_id = booking_id
        self.__status = status
        self.__created_on = created_on
        self.__description = description
        self.__equipment = equipment
        self.__customer = customer
        self.__slot = slot
        self.__payment = None
    
    
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

    def calculate_price(self):
        price = 0
        for Equipment in self.__equipment:
            price += Equipment.get_price()
        return price
    
    def create_payment(self,types='QRCode'):
        amount = self.calculate_price()
        if types == 'QRCode':
            self.__payment = QRCodeTransaction(amount) 
        else:
            self.__payment = Payment(amount)

    def get_booking_detail(self):
        return {
            "booking_id": self.get_booking_id(),
            "status": self.__status,
            "created_on": self.__created_on,
            "description": self.__description,
            "equipment": self.__equipment,
            "customer": self.__customer,
            "payment": self.__payment,
        }

    

class BookingHistory:
    def __init__(self):
        self.__booking = []

    # def search_booking_by_id(self,booking_id):
    #     for book in self.__booking:
    #         if book.get_booking_id() == booking_id:
    #             return book
    #     print("Not Found Booking")
    #     return "Not Found Booking"
        
    
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
            if book.get_booking_detail()['booking_id'] == booking_id:
                return book.get_booking_detail()
    
    def get_booking_by_id(self, booking_id):
        to_return = []
        for book in self.__booking:
            if str(book.get_booking_id()) == str(booking_id):
                return book
        return "NOT FOUND"

    
    def get_booking_by_customer(self, customer):
        for book in self.__booking:
            if book.get_customer() == customer:
                return book

    
    def create_payment(self, book, types='QRCode'):
        book.create_payment(types)
        return book.get_booking_detail()
    

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
    
    def get_price(self):
        return self.__price
    
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