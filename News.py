class News():
    def __init__(self, title, content, image_url, created_on, status):
        self._title = title
        self._content = content
        self._image_url = image_url
        self._created_on = created_on
        self._status = status

news1 = News("Plub winning hackathon", "Plub Khris winnig hackathon with his friends", "www.pinterest.com", 130265, "True")        

news2 = News("Ton winning hackathon", "Kitton winnig hackathon with his friends", "www.pinterest.com", 130265, "False") 

