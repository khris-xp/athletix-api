class Account:
  def __init__(self, password: str, role="customer") -> None:
    self.__password = password
    self.__role = role

  def get_password(self) -> str:
    return self.__password

  def get_role(self) -> str:
    return self.__role

  def set_password(self, password: str) -> None:
    self.__password = password
