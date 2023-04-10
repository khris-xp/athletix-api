from fastapi import APIRouter
from ..models.field import FieldModel
from ..database import stadium
from ..internal.field import Field
from ..internal.slot_date import SlotDate

router = APIRouter(
    prefix="/fields", tags=["fields"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_fields():
  return stadium.get_fields()


@router.post("/")
async def create_field(body: FieldModel):
  field = Field(body.name, body.description,
                body.price_by_slot, body.category, body.type)
  slots = [SlotDate(**slot.dict()) for slot in body.slot]
  field.add_slot(slots)
  stadium.add_field(field)
  return field
