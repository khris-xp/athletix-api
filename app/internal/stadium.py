class Stadium:
  def __init__(self) -> None:
    self.__category = []
    self.__news = []
    self.__user = []

  def add_news(self, news):
    self.__news.append(news)
    return self.__news

  def get_news(self):
    return [news.to_dict() for news in self.__news]

  def get_news_by_id(self, id: str):
    for news in self.__news:
      if news.get_id() == id:
        return news.to_dict()
    return None

  def get_news_by_title(self, title: str):
    for news in self.__news:
      if news.get_title() == title:
        return news.to_dict()
    return None

  def update_news(self, id: str, body: dict):
    for news in self.__news:
      if news.get_id() == id:
        news.set_title(body.get("title"))
        news.set_content(body.get("content"))
        news.set_image_url(body.get("image_url"))
        news.set_draft(body.get("draft"))
        news.set_updated_at()
        return news.to_dict()
    return None

  def delete_news(self, id: str):
    for news in self.__news:
      if news.get_id() == id:
        self.__news.remove(news)
        return "Delete news successfully"
    return None
