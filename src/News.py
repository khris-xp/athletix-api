class News():
    def __init__(self, title, content, image_url, created_on, status):
        self.__title = title
        self.__content = content
        self.__image_url = image_url
        self.__created_on = created_on
        self.__status = status

news1 = News("Plub winning hackathon", "Plub Khris winnig hackathon with his friends", "www.pinterest.com", 130265, "True")        

news2 = News("Ton winning hackathon", "Kitton winnig hackathon with his friends", "www.pinterest.com", 130265, "False") 

