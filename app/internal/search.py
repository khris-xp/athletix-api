from abc import ABC, abstractmethod


class Search(ABC):

  @abstractmethod
  def search_fields_by_category_and_date(self, category: str, date: str):
    pass
