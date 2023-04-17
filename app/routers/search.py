from fastapi import APIRouter, HTTPException, status, Depends
from ..database.database import stadium
from ..models.search import CheckSlot
router = APIRouter(
    prefix="/search", tags=["search"], responses={404: {"description": "Not found"}})


@router.get("/")
async def search(category: str, date: str):
  return stadium.search_fields_by_category_and_date(category, date)

@router.get("/slot")
async def searchSlot(field_id: str, date: str):
  return stadium.search_slots_by_field_id_and_date(field_id, date)

