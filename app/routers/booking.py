from fastapi import APIRouter

router = APIRouter(prefix="/booking",
                   tags=["booking"], responses={404: {"description": "Not found"}})


@router.post("/")
async def create_booking():
  return {"message": "Book a new appointment"}


@router.get("/history")
async def get_history():
  return {"message": "Get booking history"}
