class Account:
  def __init__(self, password: str, role="user") -> None:
    self.__password = password
    self.__role = role

  def to_dict(self) -> dict:
    return {
        key.replace('_Account__', ''): value
        for key, value in self.__dict__.items()
    }

  def get_password(self) -> str:
    return self.__password

  def get_role(self) -> str:
    return self.__role

  def set_password(self, password: str) -> None:
    self.__password = password
