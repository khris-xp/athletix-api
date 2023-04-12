from fastapi import APIRouter, HTTPException, status, Depends
from ..database.database import stadium

router = APIRouter(
    prefix="/search", tags=["search"], responses={404: {"description": "Not found"}})


@router.get("/")
async def search(type: str, date: str):
  return "search"
