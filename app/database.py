from .internal.stadium import Stadium
from .constants.user import admin1, admin2, frontdesk1, frontdesk2, customer1, customer2
from .constants.news import news_1, news_2, news_3

stadium = Stadium()

stadium.add_user(admin1)
stadium.add_user(admin2)
stadium.add_user(frontdesk1)
stadium.add_user(frontdesk2)
stadium.add_user(customer1)
stadium.add_user(customer2)

stadium.add_news(news_1)
stadium.add_news(news_2)
stadium.add_news(news_3)
