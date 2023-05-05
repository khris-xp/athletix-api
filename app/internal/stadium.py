from copy import copy


class Stadium:
  def __init__(self) -> None:
    self.__news_collection = []
    self.__equipments_collection = []
    self.__users_collection = []
    self.__fields_collection = []
    self.__bookings_collection = []

  def add_news(self, news: dict) -> dict:
    self.__news_collection.append(news)
    return news

  def get_news(self) -> list[dict]:
    return [news for news in self.__news_collection]

  def get_news_by_id(self, id: str) -> dict | None:
    for news in self.__news_collection:
      if news.get_id() == id:
        return news
    return None

  def get_news_by_title(self, title: str) -> dict | None:
    for news in self.__news_collection:
      if news.get_title() == title:
        return news
    return None

  def update_news(self, id: str, update_news: dict) -> dict | None:
    for news in self.__news_collection:
      if news.get_id() == id:
        news.set_title(update_news['title'])
        news.set_content(update_news['content'])
        news.set_image_url(update_news['image_url'])
        news.set_updated_at()
        return news
    return None

  def delete_news(self, id: str) -> str | None:
    for index, news in enumerate(self.__news_collection):
      if news.get_id() == id:
        self.__news_collection.pop(index)
        return "Delete news successfully"
    return None

  def add_equipment(self, equipment: dict) -> dict:
    self.__equipments_collection.append(equipment)
    return equipment

  def get_equipments(self) -> list[dict]:
    return [equipment for equipment in self.__equipments_collection]

  def get_equipment_by_id(self, id: str) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_id() == id:
        return equipment
    return None

  def get_equipment_by_name(self, name: str) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_name() == name:
        return equipment
    return None

  def get_equipments_by_category(self, category: str) -> list[dict]:
    return [equipment for equipment in self.__equipments_collection if equipment.get_category() == category]

  def update_equipment(self, id: str, update_equipment: dict) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_id() == id:
        equipment.set_name(update_equipment['name'])
        equipment.set_price_per_unit(update_equipment['price_per_unit'])
        equipment.set_quantity(update_equipment['quantity'])
        equipment.set_category(update_equipment['category'])
        return equipment
    return None

  def delete_equipment(self, id: str) -> str | None:
    for index, equipment in enumerate(self.__equipments_collection):
      if equipment.get_id() == id:
        self.__equipments_collection.pop(index)
        return "Delete equipment successfully"
    return None

  def add_user(self, user: dict) -> dict:
    self.__users_collection.append(user)
    return user

  def get_users(self) -> list[dict]:
    return [user for user in self.__users_collection]

  def get_user_by_email(self, email: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_email() == email:
        return user
    return None

  def get_user_by_fullname(self, fullname: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_fullname() == fullname:
        return user
    return None

  def get_user_by_phone_number(self, phone_number: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_phone_number() == phone_number:
        return user
    return None

  def get_user_by_id(self, id: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_id() == id:
        return user
    return None

  def update_user(self, id: str, update_user: dict) -> dict | None:
    for user in self.__users_collection:
      if user.get_id() == id:
        user.set_account(update_user['account'])
    return None

  def add_field(self, field: dict) -> dict:
    self.__fields_collection.append(field)
    return field

  def get_fields(self) -> list[dict]:
    return [field for field in self.__fields_collection]

  def get_field_by_id(self, id: str) -> dict | None:
    for field in self.__fields_collection:
      if field.get_id() == id:
        return field
    return None

  def get_field_by_name(self, name: str) -> dict | None:
    for field in self.__fields_collection:
      if field.get_name() == name:
        return field
    return None

  def update_field(self, id: str, update_field: dict) -> dict | None:
    for field in self.__fields_collection:
      if field.get_id() == id:
        field.set_name(update_field['name'])
        field.set_description(update_field['description'])
        field.set_price_by_slot(update_field['price_by_slot'])
        field.set_category(update_field['category'])
        field.set_type(update_field['type'])
        field.set_image(update_field['image'])
        return field
    return None

  def delete_field(self, id: str) -> str | None:
    for index, field in enumerate(self.__fields_collection):
      if field.get_id() == id:
        self.__fields_collection.pop(index)
        return "Delete field successfully"
    return None

  def search_slots_by_field_id_and_date(self, field_id: str, date: str) -> list[dict]:
    for field in self.__fields_collection:
      if field.get_id() == field_id:
        return field.get_booking_slots_by_date(date)
    return []

  def get_bookings(self):
    return [booking for booking in self.__bookings_collection]

  def get_booking_by_id(self, id: str) -> dict | None:
    for booking in self.__bookings_collection:
      if booking.get_id() == id:
        return booking
    return None

  def get_bookings_by_user(self, user_id: str) -> list[dict]:
    return [booking for booking in self.__bookings_collection if booking.get_customer()['id'] == user_id]

  def get_bookings_by_field(self, field_id: str) -> list[dict]:
    return [booking for booking in self.__bookings_collection if booking.get_field()['id'] == field_id]

  def get_bookings_by_equipment(self, equipment_id: str) -> list[dict]:
    return [booking for booking in self.__bookings_collection if equipment_id in [equipment['id'] for equipment in booking.get_equipments()]]

  def add_booking(self, booking: dict) -> dict:
    self.__bookings_collection.append(booking)
    return booking

  def delete_booking(self, booking_id: str) -> str | None:
    for index, booking in enumerate(self.__bookings_collection):
      if booking.get_id() == booking_id:
        self.__bookings_collection.pop(index)
        return "Delete booking successfully"
    return None
