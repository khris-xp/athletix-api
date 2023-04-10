class Stadium:
  def __init__(self) -> None:
    self.__news_collection = []
    self.__equipments_collection = []
    self.__users_collection = []
    self.__fields_collection = []

  def add_news(self, news: dict) -> dict:
    self.__news_collection.append(news)
    return news

  def get_news(self) -> list[dict]:
    return [news for news in self.__news_collection]

  def get_news_by_id(self, id: str) -> dict | None:
    return next((news for news in self.__news_collection if news.get_id() == id), None)

  def get_news_by_title(self, title: str) -> dict | None:
    return next((news for news in self.__news_collection if news.get_title() == title), None)

  def update_news(self, id: str, body: dict) -> dict | None:
    return next((news.set_updated_at() or news for news in self.__news_collection if news.get_id() == id and all(hasattr(news, f"set_{key}") and getattr(news, f"set_{key}")(value) or True for key, value in body.items())), None)

  def delete_news(self, id: str) -> str | None:
    return next((self.__news_collection.pop(index) or "Delete news successfully" for index, news in enumerate(self.__news_collection) if news.get_id() == id), None)

  def add_equipment(self, equipment: dict) -> dict:
    self.__equipments_collection.append(equipment)
    return equipment

  def get_equipments(self) -> list[dict]:
    return [equipment for equipment in self.__equipments_collection]

  def get_equipment_by_id(self, id: str) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_id() == id), None)

  def get_equipment_by_name(self, name: str) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_name() == name), None)

  def update_equipment(self, id: str, body: dict) -> dict | None:
    return next((equipment for equipment in self.__equipments_collection if equipment.get_id() == id and all(hasattr(equipment, f"set_{key}") and getattr(equipment, f"set_{key}")(value) or True for key, value in body.items())), None)

  def delete_equipment(self, id: str) -> str | None:
    return next((self.__equipments_collection.pop(index) or "Delete equipment successfully" for index, equipment in enumerate(self.__equipments_collection) if equipment.get_id() == id), None)

  def add_user(self, user: dict) -> dict:
    self.__users_collection.append(user)
    return user

  def get_users(self) -> list[dict]:
    users_list = []
    for user in self.__users_collection:
      user_dict = user.to_dict()
      account_dict = user.get_account().to_dict()
      user_dict['account'] = account_dict
      users_list.append(user_dict)
    return users_list

  def get_user_by_email(self, email: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_email() == email:
        user_dict = user.to_dict()
        account_dict = user.get_account().to_dict()
        user_dict['account'] = account_dict
        return user_dict
    return None

  def get_user_by_fullname(self, fullname: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_fullname() == fullname:
        user_dict = user.to_dict()
        account_dict = user.get_account().to_dict()
        user_dict['account'] = account_dict
        return user_dict
    return None

  def get_user_by_phone_number(self, phone_number: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_phone_number() == phone_number:
        user_dict = user.to_dict()
        account_dict = user.get_account().to_dict()
        user_dict['account'] = account_dict
        return user_dict
    return None

  def get_user_by_id(self, id: str) -> dict | None:
    for user in self.__users_collection:
      if user.get_id() == id:
        user_dict = user.to_dict()
        account_dict = user.get_account().to_dict()
        user_dict['account'] = account_dict
        return user_dict
    return None

  def add_field(self, field: dict) -> dict:
    self.__fields_collection.append(field)
    slot_list = []
    for slot in field.get_slots():
      slot_list.append(slot.to_dict())
    field_dict = field.to_dict()
    field_dict['slots'] = slot_list
    return field_dict

  def get_fields(self) -> list[dict]:
    fields_list = []
    for field in self.__fields_collection:
      slot_list = []
      for slot in field.get_slots():
        slot_list.append(slot.to_dict())
      field_dict = field.to_dict()
      field_dict['slots'] = slot_list
      fields_list.append(field_dict)
    return fields_list

  def get_field_by_id(self, id: str) -> dict | None:
    for field in self.__fields_collection:
      if field.get_id() == id:
        slot_list = []
        for slot in field.get_slots():
          slot_list.append(slot.to_dict())
        field_dict = field.to_dict()
        field_dict['slots'] = slot_list
        return field_dict
    return None

  def get_field_by_name(self, name: str) -> dict | None:
    for field in self.__fields_collection:
      if field.get_name() == name:
        slot_list = []
        for slot in field.get_slots():
          slot_list.append(slot.to_dict())
        field_dict = field.to_dict()
        field_dict['slots'] = slot_list
        return field_dict
    return None

  def update_field(self, id: str, body: dict) -> dict | None:
    for field in self.__fields_collection:
      if field.get_id() == id:
        field.set_name(body["name"])
        field.set_description(body['description'])
        field.set_price_by_slot(body['price_by_slot'])
        field.set_category(body['category'])
        field.set_type(body['type'])
        field.set_slots(body['slots'])
        return field.to_dict()
    return None

  def delete_field(self, id: str) -> str | None:
    for field in self.__fields_collection:
      if field.get_id() == id:
        self.__fields_collection.remove(field)
        return "Delete field successfully"
    return None
