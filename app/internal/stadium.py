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
    for news in self.__news_collection:
      if news.get_id() == id:
        return news
    return None

  def get_news_by_title(self, title: str) -> dict | None:
    for news in self.__news_collection:
      if news.get_title() == title:
        return news
    return None

  def update_news(self, id: str, body: dict) -> dict | None:
    for news in self.__news_collection:
      if news.get_id() == id:
        for key in body:
          if hasattr(news, f"set_{key}"):
            getattr(news, f"set_{key}")(body[key])
        news.set_updated_at()
        return news
    return None

  def delete_news(self, id: str) -> str | None:
    for index, news in enumerate(self.__news_collection):
      if news.get_id() == id:
        del self.__news_collection[index]
        return "Delete news successfully"
    return None

  def add_equipment(self, equipment: dict) -> dict:
    self.__equipments_collection.append(equipment)
    return equipment.to_dict()

  def get_equipments(self) -> list[dict]:
    return [equipment.to_dict() for equipment in self.__equipments_collection]

  def get_equipment_by_id(self, id: str) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_id() == id:
        return equipment.to_dict()
    return None

  def get_equipment_by_name(self, name: str) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_name() == name:
        return equipment.to_dict()
    return None

  def update_equipment(self, id: str, body: dict) -> dict | None:
    for equipment in self.__equipments_collection:
      if equipment.get_id() == id:
        equipment.set_name(body["name"])
        equipment.set_price(body["price"])
        equipment.set_quantity(body["quantity"])
        return equipment.to_dict()
    return None

  def delete_equipment(self, id: str) -> str | None:
    for equipment in self.__equipments_collection:
      if equipment.get_id() == id:
        self.__equipments_collection.remove(equipment)
        return "Delete equipment successfully"
    return None

  def add_user(self, user: dict) -> dict:
    self.__users_collection.append(user)
    user_dict = user.to_dict()
    account_dict = user.get_account().to_dict()
    user_dict['account'] = account_dict
    return user_dict

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
