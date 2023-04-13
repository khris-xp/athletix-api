from ..internal.stadium import Stadium
from ..internal.booking_history import BookingHistory
from ..constants.users import admin1, admin2, frontdesk1, frontdesk2, customer1, customer2
from ..constants.news import news_1, news_2, news_3
from ..constants.fields import football1_field, football2_field, football3_field, basketball1_field, basketball2_field, basketball3_field, badminton1_field, badminton2_field, badminton3_field
from ..constants.equipments import football_equipment, basketball_equipment, shuttlecock_equipment, vest_equipment

stadium = Stadium()
booking_history = BookingHistory()

stadium.add_user(admin1)
stadium.add_user(admin2)
stadium.add_user(frontdesk1)
stadium.add_user(frontdesk2)
stadium.add_user(customer1)
stadium.add_user(customer2)

stadium.add_news(news_1)
stadium.add_news(news_2)
stadium.add_news(news_3)

stadium.add_field(football1_field)
stadium.add_field(football2_field)
stadium.add_field(football3_field)
stadium.add_field(basketball1_field)
stadium.add_field(basketball2_field)
stadium.add_field(basketball3_field)
stadium.add_field(badminton1_field)
stadium.add_field(badminton2_field)
stadium.add_field(badminton3_field)

stadium.add_equipment(football_equipment)
stadium.add_equipment(basketball_equipment)
stadium.add_equipment(shuttlecock_equipment)
stadium.add_equipment(vest_equipment)
