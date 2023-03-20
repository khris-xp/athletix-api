from Slot import SlotDate

class Field:
  def __init__(self, name, description, price_by_slot, category, types):
    self.__name = name
    self.__description = description
    self.__price_by_slot = price_by_slot
    self.__category = category
    self.__type = types

  def get_slot(self, field, date):
    pass


  def get_field_detail(self):
    return self.name, self.description, self.price_by_slot, self.category, self.type

football1 = Field("Football 1", "Football field 1", 100, "Football", "Outdoor")
football2 = Field("Football 2", "Football field 2", 100, "Football", "Outdoor")


