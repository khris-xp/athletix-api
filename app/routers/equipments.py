from fastapi import APIRouter, status, HTTPException, Depends
from ..database.database import stadium
from ..models.equipment import EquipmentModel, SearchEquipmentModel
from ..internal.football import FootBall
from ..internal.shuttlecock import ShuttleCock
from ..internal.basketball import BasketBall
from ..internal.vest import Vest
from ..utils.dependencies import get_current_user, roles_required

router = APIRouter(prefix="/equipments",
                   tags=["equipments"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_equipments():
  return [equipment.to_dict() for equipment in stadium.get_equipments()]


@router.get("/{equipment_id}")
async def get_equipment(equipment_id: str):
  equipment = stadium.get_equipment_by_id(equipment_id)

  if equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return equipment.to_dict()


@router.get("/search/")
async def get_equipment_by_category(category: str):

  return [equipment.to_dict() for equipment in stadium.get_equipments_by_category(category)]


@router.post("/{equipment_type}", status_code=status.HTTP_201_CREATED)
@roles_required(["admin"])
async def add_equipment(equipment_type: str, body: EquipmentModel, user=Depends(get_current_user)):
  equipment_exist = stadium.get_equipment_by_name(body.name)

  if equipment_exist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Equipment already exists")

  equipment = None
  if equipment_type == "football":
    equipment = FootBall(**body.dict())
  elif equipment_type == "vest":
    equipment = Vest(**body.dict())
  elif equipment_type == "shuttlecock":
    equipment = ShuttleCock(**body.dict())
  elif equipment_type == "basketball":
    equipment = BasketBall(**body.dict())
  else:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Equipment type is not supported")

  new_equipment = stadium.add_equipment(equipment)

  return new_equipment.to_dict()


@router.put("/{equipment_id}")
@roles_required(["admin"])
async def update_equipment(equipment_id: str, equipment: EquipmentModel, user=Depends(get_current_user)):
  update_equipment = stadium.update_equipment(equipment_id, equipment.dict())

  if update_equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return update_equipment.to_dict()


@router.delete("/{equipment_id}")
@roles_required(["admin"])
async def delete_equipment(equipment_id: str, user=Depends(get_current_user)):
  hasEquipmentBooked = stadium.get_bookings_by_equipment(equipment_id)

  if len(hasEquipmentBooked) > 0:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Equipment has been booked")

  delete_equipment = stadium.delete_equipment(equipment_id)

  if delete_equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete equipment successfully")
