from fastapi import APIRouter

router = APIRouter(
    prefix="/fields", tags=["fields"], responses={404: {"description": "Not found"}})


@router.get("/search")
async def search_field():
  return {"message": "Search for available fields"}


@router.get("/slot")
async def get_slot():
  return {"message": "Get slot"}
