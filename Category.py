from Field import football1, football2 , basketball1


class Category:
  def __init__(self):
    self.__category = {}

  def search_field(self, date, category):
    pass

  def add_category(self, field, category_name):
    if self.__category.get(category_name) is None:
      self.__category[category_name] = [field]
    else:
      self.__category[category_name].append(field)

  def get_category(self, category_name):
    return self.__category[category_name]


category = Category()

category.add_category(football1, "football")
category.add_category(football2, "football")
category.add_category(basketball1, "basketball")

