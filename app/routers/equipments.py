from fastapi import APIRouter, status, HTTPException
from ..database import stadium
from ..models.equipment import EquipmentModel
from ..internal.football import FootBall
from ..internal.vest import Vest

router = APIRouter(prefix="/equipments",
                   tags=["equipments"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_equipments():
  return stadium.get_equipments()


@router.get("/{equipment_id}")
async def get_equipment(equipment_id: str):
  equipment = stadium.get_equipment_by_id(equipment_id)

  if equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return equipment


@router.post("/football", status_code=status.HTTP_201_CREATED)
async def add_football_equipment(body: EquipmentModel):
  equipmentExist = stadium.get_equipment_by_name(body.name)

  if equipmentExist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Football already existed")

  football = FootBall(**body.dict())

  new_football = stadium.add_equipment(football)
  return new_football


@router.post("/vest", status_code=status.HTTP_201_CREATED)
async def add_vest_equipment(body: EquipmentModel):
  vestExist = stadium.get_equipment_by_name(body.name)

  if vestExist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Vest already existed")

  vest = Vest(**body.dict())

  new_vest = stadium.add_equipment(vest)
  return new_vest


@router.patch("/{equipment_id}")
async def update_equipment(equipment_id: str, equipment: EquipmentModel):
  update_equipment = stadium.update_equipment(equipment_id, equipment.dict())

  if update_equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return update_equipment


@router.delete("/{equipment_id}")
async def delete_equipment(equipment_id: str):
  delete_equipment = stadium.delete_equipment(equipment_id)

  if delete_equipment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Equipment not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete equipment successfully")
