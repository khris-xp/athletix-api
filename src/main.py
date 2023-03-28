from Stadium import stadium
from Person import Customer,Admin
from Storage import Stroage
from Booking import BookingHistory,ball1,ball2,ball3,ball4,vest1,vest2,vest3,vest4,Vest,Football



if __name__ == '__main__':
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
  
  #print(stadium.search_slot("badawdsketball", "2021-01-01"))
  
  print("======================  SEARCH SLOT ====================")
  print(stadium.search_slot("basketball", "2021-01-01"))
  
  
  
  print("======================  BOOKING.... ====================")
  slot = stadium.get_exactly_slot("basketball", "2021-01-01", "10:00", "11:00")
  selected = stroage.get_equipment(Football,4)
  bookinghistory.create_booking("let me book dddda",slot,customer,selected)
  
  
  
  print("====================== SHOW BOOKING HISTORY =============")
  print(bookinghistory.show_booking_history())
  
  
  
  print("====================== SHOW EQUIPMENT HISTORY =================")
  stroage.show_equipment()
  
  
  print("======================  SEARCH SLOT AGIAN 2 ====================")
  print(stadium.search_slot("basketball", "2021-01-01"))
  
  
  #print(stroage.show_equipment(Football))
  