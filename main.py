from Stadium import stadium
from Person import Customer

if __name__ == '__main__':
  customer = Customer("customer", "customer@gmail.com", "0123456789",
                      "Hanoi", "01/01/2000", "customer2", "9154064564")
  
  #print(stadium.search_slot("badawdsketball", "2021-01-01"))
  print(stadium.search_slot("basketball", "2021-01-01"))

