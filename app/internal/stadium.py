from .search import Search


class Stadium(Search):
  def __init__(self) -> None:
    self.__news_collection = []
    self.__equipments_collection = []
    self.__users_collection = []
    self.__fields_collection = []
    self.__booking_collection = []

  def add_news(self, news: dict) -> dict:
    return self.__news_collection.append(news) or news

  def get_news(self) -> list[dict]:
    return [news for news in self.__news_collection]

  def get_news_by_id(self, id: str) -> dict | None:
    return next((news for news in self.__news_collection if news.get_id() == id), None)

  def get_news_by_title(self, title: str) -> dict | None:
    return next((news for news in self.__news_collection if news.get_title() == title), None)

  def update_news(self, id: str, update_news: dict) -> dict | None:
    return next((news.set_updated_at() or news for news in self.__news_collection if news.get_id() == id and all(hasattr(news, f"set_{key}") and getattr(news, f"set_{key}")(value) or True for key, value in update_news.items())), None)

  def delete_news(self, id: str) -> str | None:
    return next((self.__news_collection.pop(index) or "Delete news successfully" for index, news in enumerate(self.__news_collection) if news.get_id() == id), None)

  def add_equipment(self, equipment: dict) -> dict:
    return self.__equipments_collection.append(equipment) or equipment

  def get_equipments(self) -> list[dict]:
    return [equipment for equipment in self.__equipments_collection]

  def get_equipment_by_id(self, id: str) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_id() == id), None)

  def get_equipment_by_name(self, name: str) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_name() == name), None)

  def update_equipment(self, id: str, update_equipment: dict) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_id() == id and all(hasattr(equipment, f"set_{key}") and getattr(equipment, f"set_{key}")(value) or True for key, value in update_equipment.items())), None)

  def delete_equipment(self, id: str) -> str | None:
    return next((self.__equipments_collection.pop(index) or "Delete equipment successfully" for index, equipment in enumerate(self.__equipments_collection) if equipment.get_id() == id), None)

  def add_user(self, user: dict) -> dict:
    return self.__users_collection.append(user) or user

  def get_users(self) -> list[dict]:
    return [user for user in self.__users_collection]

  def get_user_by_email(self, email: str) -> dict | None:
    return next((user for user in self.__users_collection if user.get_email() == email), None)

  def get_user_by_fullname(self, fullname: str) -> dict | None:
    return next((user for user in self.__users_collection if user.get_fullname() == fullname), None)

  def get_user_by_phone_number(self, phone_number: str) -> dict | None:
    return next((user for user in self.__users_collection if user.get_phone_number() == phone_number), None)

  def get_user_by_id(self, id: str) -> dict | None:
    return next((user for user in self.__users_collection if user.get_id() == id), None)

  def update_user(self, id: str, update_user: dict) -> dict | None:
    return next((user for user in self.__users_collection if user.get_id() == id and all(hasattr(user, f"set_{key}") and getattr(user, f"set_{key}")(value) or True for key, value in update_user.items())), None)

  def add_field(self, field: dict) -> dict:
    return self.__fields_collection.append(field) or field

  def get_fields(self) -> list[dict]:
    return [field for field in self.__fields_collection]

  def get_field_by_id(self, id: str) -> dict | None:
    return next((field for field in self.__fields_collection if field.get_id() == id), None)

  def get_field_by_name(self, name: str) -> dict | None:
    return next((field for field in self.__fields_collection if field.get_name() == name), None)

  def update_field(self, id: str, update_field: dict) -> dict | None:
    return next((field for field in self.__fields_collection if field.get_id() == id and all(hasattr(field, f"set_{key}") and getattr(field, f"set_{key}")(value) or True for key, value in update_field.items())), None)

  def delete_field(self, id: str) -> str | None:
    return next((self.__fields_collection.pop(index) or "Delete field successfully" for index, field in enumerate(self.__fields_collection) if field.get_id() == id), None)

  def search_fields_by_category_and_date(self, category: str, date: str) -> list[dict]:
    return [field for field in self.__fields_collection if field.get_category().lower() == category.lower() and (any(slot.get_date() == date for slot in field.get_booking_slots()) or not any(slot.get_date() for slot in field.get_booking_slots()))]
