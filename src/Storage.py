
from src.Booking import Vest,Football

class Stroage:
    def __init__(self):
        self.__equipment = []
        
        
    def show_equipment(self):
        to_return = []
        for equipment in self.__equipment:
            print(equipment.get_details())
            to_return.append(equipment.get_details()) 
        return to_return
    
    def add(self, equipment):
        self.__equipment.append(equipment)
        
    def count_equipment(self,equipment_type):
        count = 0
        for equipment in self.__equipment:
            if isinstance(equipment, eval(equipment_type)):
                count += 1
        return count

        
    def available_equipment(self,equipment_type):
        equipment_list = []
        for equipment in self.__equipment:

            if isinstance(equipment, eval(equipment_type)) and equipment.get_status() == 'available':
                equipment_list.append(equipment)
        return equipment_list

    def get_equipment(self,equipment_type, amount):
        if amount > len(self.available_equipment(equipment_type)):
            print("Not Enough Equipment available")
            return "Not Enough Equipment available"
        else:
            equipment_list = []
            for equipment in self.available_equipment(equipment_type):
                    #equipment.get_book()
                    equipment_list.append(equipment)
            return equipment_list[:amount]
                    
        


    
        
    