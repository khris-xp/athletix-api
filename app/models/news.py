from pydantic import BaseModel


class NewsModel(BaseModel):
  title: str
  content: str
  image_url: str
  author: str
  draft: bool
