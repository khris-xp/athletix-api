from fastapi import APIRouter, HTTPException, status, Depends
from ..database import stadium
from ..internal.news import News
from ..models.news import NewsModel
from ..dependencies import get_current_user

router = APIRouter(
    prefix="/news", tags=["news"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_news():
  return stadium.get_news()


@router.get("/{id}")
async def get_news_by_id(id: str):
  news = stadium.get_news_by_id(id)
  if news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
  return news


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_news(body: NewsModel, current_user = Depends(get_current_user)):
  news = News(**body.dict())
  
  if stadium.get_news_by_title(body.title) is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="News already existed")

  new_news = stadium.add_news(news)
  return new_news


@router.patch("/{id}")
async def update_news(id: str, body: NewsModel, current_user = Depends(get_current_user)):
  updated_news = stadium.update_news(id, body.dict())

  if updated_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="News not found")

  # TODO: check news author and current user

  return updated_news


@router.delete("/{id}")
async def delete_news(id: str):
  deleted_news = stadium.delete_news(id)
  if deleted_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="News not found")

  # TODO: check news author and current user

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete news successfully")
