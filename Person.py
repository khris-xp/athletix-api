class Person:
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    self.__fullname = fullname
    self.__email = email
    self.__phone_number = phone_number
    self.__address = address
    self.__birth_date = birth_date
    self.__emergency_contact_fullname = emergency_contact_fullname
    self.__emergency_contact_phone_number = emergency_contact_phone_number

  def add_booking(self, slot, description):
    pass

  def get_booking_detail(self):
    pass

  def search_booking_by_id(self, id):
    pass


class FrontDesk(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)

  def approve_booking(self):
    pass


class Customer(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)


class Admin(Person):
  def __init__(self, fullname, email, phone_number, address, birth_date, emergency_contact_fullname, emergency_contact_phone_number):
    super().__init__(fullname, email, phone_number, address, birth_date,
                     emergency_contact_fullname, emergency_contact_phone_number)

  def add_field(self, name, description, price_by_slot, category, type, slot):
    pass

  def edit_field(self, name, description, price_by_slot, category, type, slot):
    pass

  def delete_field(self):
    pass

  def approve_booking(self):
    pass

  def add_news(self, title, content, image_url, created_on, status):
    pass

  def edit_news(self, title, content, image_url, created_on, status):
    pass

  def delete_news(self):
    pass

  def add_slot(self, created_on, start_time, end_time):
    pass

  def edit_slot(self, created_on, start_time, end_time):
    pass

  def delete_slot(self):
    pass

  def block_user(self):
    pass


class Guest:
  def __init__(self):
    pass

  def register_account(self):
    pass

  def login_account(self):
    pass

  def check_register(self):
    pass

  def check_login(self):
    pass


admin = Admin("admin", "admin@gmail.com", "0123456789", "Hanoi", "01/01/2000", "admin2", "9154064564")

customer = Customer("customer", "customer@gmail.com", "0123456789", "Hanoi", "01/01/2000", "customer2", "9154064564")

frontdesk = FrontDesk("frontdesk", "frontdesk@gmail.com", "0123456789", "Hanoi", "01/01/2000", "frontdesk2", "9154064564")