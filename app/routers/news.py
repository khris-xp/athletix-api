from fastapi import APIRouter, HTTPException, status, Depends
from ..database.database import stadium
from ..internal.news import News
from ..models.news import NewsModel
from ..utils.dependencies import role_required
from ..utils.dependencies import get_current_user

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
@role_required("admin")
async def create_news(body: NewsModel,  user=Depends(get_current_user)):
  news_exist = stadium.get_news_by_title(body.title)

  if news_exist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="News already existed")

  news = News(**body.dict())

  new_news = stadium.add_news(news)
  return new_news


@router.patch("/{id}")
@role_required("admin")
async def update_news(id: str, body: NewsModel, user=Depends(get_current_user)):
  updated_news = stadium.update_news(id, body.dict())

  if updated_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="News not found")

  return updated_news


@router.delete("/{id}")
@role_required("admin")
async def delete_news(id: str, user=Depends(get_current_user)):
  deleted_news = stadium.delete_news(id)

  if deleted_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="News not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete news successfully")
