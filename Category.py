
class Category:
    def __init__(self):
        self.__category= {}
        self.__date = {}

    def search_field(self, date ,category):
        pass
    
category = Category()
category.__category.append("football")
category.__date.append("2021-01-01")
category.search_field("2021-01-01", "Football")
