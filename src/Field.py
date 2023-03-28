from src.Slot import slot1, slot2, slot3


class Field:
  def __init__(self, name, description, price_by_slot, category, types):
    self.__name = name
    self.__description = description
    self.__price_by_slot = price_by_slot
    self.__category = category
    self.__type = types
    self.__slot = []

  def get_slot_by_date(self, date):
    slots = []
    for slot in self.__slot:
      if slot.get_date() == date:
        slots.append(slot.get_slot_date_details())
    return slots

  def get_field_detail(self):
    return {
      "name": self.__name,
      "description": self.__description,
      "price_by_slot": self.__price_by_slot,
      "category": self.__category,
      "type": self.__type,
      "slot": self.__slot
    }

  def add_slot(self, slot):
    self.__slot.append(slot)
  
  def get_name(self):
    return self.__name


football1 = Field("Football 1", "Football field 1", 100, "Football", "Outdoor")
football2 = Field("Football 2", "Football field 2", 100, "Football", "Indoor")

basketball1 = Field("Basketball 1", "Basketball field 1", 100, "Basketball", "Outdoor")

football1.add_slot(slot1)
football1.add_slot(slot2)
football1.add_slot(slot3)

football2.add_slot(slot1)
football2.add_slot(slot2)
football2.add_slot(slot3)

basketball1.add_slot(slot1)
basketball1.add_slot(slot2)
basketball1.add_slot(slot3)

# print(football1.get_slot_by_date("2021-01-01"))
# print(football1.get_slot_by_date("2021-01-02"))
