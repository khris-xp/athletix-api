from ..internal.admin import Admin
from ..internal.frontdesk import FrontDesk
from ..internal.customer import Customer
from ..internal.account import Account

admin1_account = Account(
    password="$2b$12$vqNRXIAxokSIu/vekoeGquHyXHbtVCvyiRqHYoeOGUgYn7VITURa6", role="admin")
admin2_account = Account(
    password="$2b$12$p2cg2n0/wiMhNphy9YH5c.dE.I39bAPC7uPDQvhol9ZV5EghyP/we", role="admin")

frontdesk1_account = Account(
    password="$2b$12$kdS2EhL2Kgrfyr5/zN4JMe9eyXtlR8mOJIcQJ12JuT/0QR.tj/H3C", role="frontdesk")
frontdesk2_account = Account(
    password="$2b$12$K1/Gv5kMVsTwLm1aGwwy8.bJwMtqoRz30hmUSR3vGYEHHaCAt0jw6", role="frontdesk")

customer1_account = Account(
    password="$2b$12$NLTs82cyroy1uEWTp4k7w.1DZcIwyYqBPeKkZUq4frrbhIz5nG0uW"
)
customer2_account = Account(
    password="$2b$12$YcYXdKCAI5DbV3sGXWC4H.PySr0MTZgxgTvJU09VZG3XYT04E2M4W"
)

admin1 = Admin(
    fullname="admin1",
    email="admin1@gmail.com",
    phone_number="1234567690",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_fullname="test1",
    emergency_contact_phone_number="0231654564",
    account=admin1_account
)
admin2 = Admin(
    fullname="admin2",
    email="admin2@gmail.com",
    phone_number="5234567790",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_fullname="test1",
    emergency_contact_phone_number="0231654564",
    account=admin2_account
)

frontdesk1 = FrontDesk(
    fullname="frontdesk1",
    email="frontdesk1@gmail.com",
    phone_number="1234567790",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_phone_number="0231654564",
    emergency_contact_fullname="test1",
    account=frontdesk1_account
)
frontdesk2 = FrontDesk(
    fullname="frontdesk2",
    email="frontdesk2@gmail.com",
    phone_number="1334567690",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_fullname="test1",
    emergency_contact_phone_number="0231654564",
    account=frontdesk2_account
)

customer1 = Customer(
    fullname="customer1",
    email="customer1@gmail.com",
    phone_number="1635567690",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_fullname="test1",
    emergency_contact_phone_number="0231654564",
    account=customer1_account
)
customer2 = Customer(
    fullname="customer2",
    email="customer2@gmail.com",
    phone_number="1636567690",
    address="test",
    birth_date="2022-12-27",
    emergency_contact_fullname="test1",
    emergency_contact_phone_number="0231654564",
    account=customer2_account
)
