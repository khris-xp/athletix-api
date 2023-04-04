from fastapi import APIRouter

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_users():
  return {"message": "Get all users"}


@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
  return {"message": f"Get user with id {user_id}"}
