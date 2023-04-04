from fastapi import APIRouter

router = APIRouter(prefix="/equipments",
                   tags=["equipments"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_equipments():
  return {"message": "Get all equipment"}
