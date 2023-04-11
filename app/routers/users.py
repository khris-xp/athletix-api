from fastapi import APIRouter, Depends, HTTPException, status
from ..database.database import stadium
from ..utils.dependencies import get_current_user, get_password_hash, verify_password
from ..models.auth import ChangePasswordModel

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})


@router.get("/profile")
async def get_profile(current_user=Depends(get_current_user)):
  return current_user


@router.post("/change-password")
async def change_password(body: ChangePasswordModel, current_user=Depends(get_current_user)):
  if not verify_password(body.old_password, current_user.get_account().get_password()):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

  current_user.get_account().set_password(get_password_hash(body.new_password))
  stadium.update_user(current_user.get_id(), {
      "account": current_user.get_account()
  })

  return {"message": "Password changed successfully"}
