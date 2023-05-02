from fastapi import APIRouter, UploadFile, File
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
