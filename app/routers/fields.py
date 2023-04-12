from fastapi import APIRouter, HTTPException, status, Depends
from ..models.field import FieldModel
from ..database import stadium
from ..internal.field import Field
from ..internal.slot_date import SlotDate
from datetime import datetime, timedelta
from ..dependencies import get_current_user, role_required

router = APIRouter(
    prefix="/fields", tags=["fields"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_fields():
  return stadium.get_fields()


@router.get("/{id}")
async def get_field(id: str):
  field = stadium.get_field_by_id(id)
  if field is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
  return field


@router.post("/", status_code=status.HTTP_201_CREATED)
@role_required("admin")
async def create_field(body: FieldModel, user=Depends(get_current_user)):
  field_exist = stadium.get_field_by_name(body.name)
  if field_exist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Field name already exists")

  field = Field(**body.dict())

  new_field = stadium.add_field(field)

  tomorrow = datetime.now() + timedelta(days=1)
  start_time = tomorrow.replace(hour=9, minute=0, second=0, microsecond=0)
  end_time = tomorrow.replace(
      day=1, hour=20, minute=0, second=0, microsecond=0) + timedelta(days=30)
  duration = timedelta(hours=1)

  while start_time < end_time:
    slot = SlotDate(start_time, start_time + duration, start_time)
    new_field.add_slot(slot)
    start_time += duration

  return new_field


@router.patch("/{id}")
@role_required("admin")
async def update_field(id: str, body: FieldModel, user=Depends(get_current_user)):
  updated_news = stadium.update_field(id, body.dict())

  if updated_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return updated_news


@router.delete("/{id}")
@role_required("admin")
async def delete_field(id: str, user=Depends(get_current_user)):
  deleted_field = stadium.delete_field(id)
  if deleted_field is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete field successfully")
