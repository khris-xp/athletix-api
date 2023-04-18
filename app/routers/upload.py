from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from ..utils.dependencies import get_current_user
from ..models.payment import PromptpayPaymentModel, CashPaymentModel
from ..database.database import booking_history
import shutil
import os
import uuid
router = APIRouter(prefix="/upload", tags=["upload"], responses={
                   404: {"description": "Not found"}})


@router.post("/")
async def upload_slip(file: UploadFile = File(...)):
  if not os.path.exists("images"):
    os.makedirs("images")
  name = str(uuid.uuid4())
  with open(f"images/{name}.png", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
  return {"filename": f"images/{name}.png"}
  
