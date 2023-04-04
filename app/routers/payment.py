from fastapi import APIRouter

router = APIRouter(prefix="/payment", tags=["payment"], responses={
                   404: {"description": "Not found"}})


@router.post("/")
async def create_payment():
  return {"message": "payment created"}
