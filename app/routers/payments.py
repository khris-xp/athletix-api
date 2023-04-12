from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["payments"], responses={
                   404: {"description": "Not found"}})


@router.post("/")
async def create_payment():
  return {"message": "payment created"}


@router.post("/cancel")
async def cancel_payment():
  return {"message": "payment cancelled"}
