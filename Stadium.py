from Category import category


class Stadium:
  def __init__(self, category):
    self.__category = category

  def search_field_by_category(self, category_name):
    return self.__category.get_category(category_name)

  
  def search_slot(self, category, date):
    fields = {}
    try:
      for field in self.search_field_by_category(category):
        fields[field.get_name()] = field.get_slot_by_date(date)
      return fields
    except:
      pass


stadium = Stadium(category)
