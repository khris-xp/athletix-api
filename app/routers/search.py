from fastapi import APIRouter, HTTPException, status, Depends
from ..database.database import stadium
router = APIRouter(
    prefix="/search", tags=["search"], responses={404: {"description": "Not found"}})


@router.get("/")
async def search(category: str, date: str):
  return [field.to_dict() for field in stadium.search_fields_by_category_and_date(category, date)]


@router.get("/slot")
async def searchSlot(field_id: str, date: str):
  return [slot.to_dict() for slot in stadium.search_slots_by_field_id_and_date(field_id, date)]
