import uuid

class Account:
  def __init__(self, password: str) -> None:
    self.__id = str(uuid.uuid4())
    self.__password = password
  