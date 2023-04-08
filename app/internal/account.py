import uuid

class Account:
  def __init__(self, password: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__password = password
    self.__role = "user"
    
  def get_id(self) -> str:
    return self.__id
  
  def get_password(self) -> str:
    return self.__password
  
  def get_role(self) -> str:
    return self.__role
  
  def set_password(self, password: str) -> None:
    self.__password = password
    
  