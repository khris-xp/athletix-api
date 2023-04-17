from src.Stadium import stadium
from src.Person import Customer, Admin
from src.Storage import Stroage
from src.Booking import BookingHistory, ball1, ball2, ball3, ball4, vest1, vest2, vest3, vest4, Vest, Football
from fastapi import FastAPI

customer = Customer("customer", "customer@gmail.com", "0123456789",
                    "Hanoi", "01/01/2000", "customer2", "9154064564")
admin = Admin("admin", "admin@gmail.com", "0123456789",
              "Hanoi", "2/4/1931", "admin2", "9154064564")

bookinghistory = BookingHistory()
stroage = Stroage()
stroage.add(ball1)
stroage.add(ball2)
stroage.add(ball3)
stroage.add(ball4)
stroage.add(vest1)
stroage.add(vest2)
stroage.add(vest3)
stroage.add(vest4)

# print(stadium.search_slot("badawdsketball", "2021-01-01"))

# print("======================  SEARCH SLOT ====================")
# print(stadium.search_slot("basketball", "2021-01-01"))

# print("======================  BOOKING.... ====================")
# slot = stadium.get_exactly_slot("basketball", "2021-01-01", "10:00", "11:00")
# selected = stroage.get_equipment(Football, 4)
# bookinghistory.create_booking("let me book dddda", "basketball", "2021-01-01", "10:00", "11:00", customer, selected)

# print("====================== SHOW BOOKING HISTORY =============")
# print(bookinghistory.show_booking_history())

# print("====================== SHOW EQUIPMENT HISTORY =================")
# stroage.show_equipment()

# print("======================  SEARCH SLOT AGIAN 2 ====================")
# print(stadium.search_slot("basketball", "2021-01-01"))

# print(stroage.show_equipment(Football))


app = FastAPI()


@app.get("/")
def root():
  return 'Hello Athetix'

@app.post("/create-payment")
def create_payment(booking_id: str, types: str):
  book = bookinghistory.get_booking_by_id(booking_id)
  return book
  #return book.create_payment(book, types)

@app.get("/book-detail")
def book(booking_id: str):
  books = bookinghistory.get_booking_by_id(booking_id)
  return books

@app.post("/create-customer")
def create_customer(name: str, email: str, phone: str, address: str, dob: str, username: str, password: str):
  return Customer(name, email, phone, address, dob, username, password)


@app.get("/search")
def search(type: str, date: str):
  return stadium.search_slot(type, date)


@app.get("/slot")
def slot(type: str, date: str, start_time: str, end_time: str):
  return stadium.get_exactly_slot(type, date, start_time, end_time)


@app.post("/booking")
def booking(description: str, category, day: str, start_time: str, end_time: str, customer: str, equipment_type: str, equipment_number : int):
  slot = stadium.get_exactly_slot(category,day, start_time, end_time)
  equipment = stroage.get_equipment(equipment_type,equipment_number)
  return bookinghistory.create_booking(description,slot,customer,equipment)

@app.get("/bookings")
def booking():
  return bookinghistory.show_booking_history()

@app.get("/equipments")
def storage():
  return stroage.show_equipment()

