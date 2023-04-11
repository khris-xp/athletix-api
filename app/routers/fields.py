from fastapi import APIRouter, HTTPException, status
from ..models.field import FieldModel
from ..database import stadium
from ..internal.field import Field
from ..internal.slot_date import SlotDate
from datetime import datetime, timedelta

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
async def create_field(body: FieldModel):
  fieldExist = stadium.get_field_by_name(body.name)
  if fieldExist is not None:
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
async def update_field(id: str, body: FieldModel):
  updated_news = stadium.update_field(id, body.dict())

  if updated_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return updated_news


@router.delete("/{id}")
async def delete_field(id: str):
  deleted_field = stadium.delete_field(id)
  if deleted_field is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete field successfully")
