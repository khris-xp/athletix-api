class Stadium:
  def __init__(self) -> None:
    self.__news = []
    self.__equipments = []

  def add_news(self, news: dict) -> dict:
    self.__news.append(news)
    return news.to_dict()

  def get_news(self) -> list[dict]:
    return [news.to_dict() for news in self.__news]

  def get_news_by_id(self, id: str) -> dict | None:
    for news in self.__news:
      if news.get_id() == id:
        return news.to_dict()
    return None

  def get_news_by_title(self, title: str) -> dict | None:
    for news in self.__news:
      if news.get_title() == title:
        return news.to_dict()
    return None

  def update_news(self, id: str, body: dict) -> dict | None:
    for news in self.__news:
      if news.get_id() == id:
        news.set_title(body["title"])
        news.set_content(body["content"])
        news.set_image_url(body["image_url"])
        news.set_draft(body["draft"])
        news.set_updated_at()
        return news.to_dict()
    return None

  def delete_news(self, id: str) -> str | None:
    for news in self.__news:
      if news.get_id() == id:
        self.__news.remove(news)
        return "Delete news successfully"
    return None
  
  def add_equipment(self, equipment: dict) -> dict:
    self.__equipments.append(equipment)
    return equipment.to_dict()
  
  def get_equipments(self) -> list[dict]:
    return [equipment.to_dict() for equipment in self.__equipments]
  
  def get_equipment_by_id(self, id: str) -> dict | None:
    for equipment in self.__equipments:
      if equipment.get_id() == id:
        return equipment.to_dict()
    return None
  
  def get_equipment_by_name(self, name: str) -> dict | None:
    for equipment in self.__equipments:
      if equipment.get_name() == name:
        return equipment.to_dict()
    return None
  
  def update_equipment(self, id: str, body: dict) -> dict | None:
    for equipment in self.__equipments:
      if equipment.get_id() == id:
        equipment.set_name(body["name"])
        equipment.set_price(body["price"])
        equipment.set_quantity(body["quantity"])
        return equipment.to_dict()
    return None
  
  def delete_equipment(self, id: str) -> str | None:
    for equipment in self.__equipments:
      if equipment.get_id() == id:
        self.__equipments.remove(equipment)
        return "Delete equipment successfully"
    return None
  
  
