from enum import Enum


class AccountStatus(Enum):
  ACTIVE, BLOCKED = 1, 2


class Account:
  def __init__(self, id, password, status):
    self.__id = id
    self.__password = password
    self.__status = status

  def check_password(self):
    pass

  def create_user(self):
    return "User created successfully with id: " + self.__id + " and password: " + self.__password + " and status: " + self.__status.name

  def logout_account(self):
    pass



account = Account("1", "password", AccountStatus.ACTIVE)

print(account.create_user())
