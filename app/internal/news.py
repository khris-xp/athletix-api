from datetime import datetime
import uuid


class News:
  def __init__(self, title: str, content: str, image_url: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__title = title
    self.__content = content
    self.__image_url = image_url
    self.__created_at = datetime.now()
    self.__updated_at = datetime.now()

  def to_dict(self) -> dict:
    return {
        key.replace("_News__", ""): value
        for key, value in self.__dict__.items()
    }

  def get_id(self) -> str:
    return self.__id

  def get_title(self) -> str:
    return self.__title

  def set_title(self, title: str) -> None:
    self.__title = title

  def set_content(self, content: str) -> None:
    self.__content = content

  def set_image_url(self, image_url: str) -> None:
    self.__image_url = image_url

  def set_updated_at(self) -> None:
    self.__updated_at = datetime.now()
