from fastapi import APIRouter, HTTPException, status, Depends
from ..models.field import FieldModel
from ..database.database import stadium
from ..internal.field import Field
from ..utils.dependencies import get_current_user, roles_required

router = APIRouter(
    prefix="/fields", tags=["fields"], responses={404: {"description": "Not found"}})


@router.get("/")
async def get_fields():
  return [field.to_dict() for field in stadium.get_fields()]


@router.get("/{id}")
async def get_field(id: str):
  field = stadium.get_field_by_id(id)
  if field is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")
  return field.to_dict()


@router.post("/", status_code=status.HTTP_201_CREATED)
@roles_required(["admin"])
async def create_field(body: FieldModel, user=Depends(get_current_user)):
  field_exist = stadium.get_field_by_name(body.name)
  if field_exist is not None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Field name already exists")

  field = Field(**body.dict())
  
  new_field = stadium.add_field(field)

  return new_field.to_dict()


@router.put("/{id}")
@roles_required(["admin"])
async def update_field(id: str, body: FieldModel, user=Depends(get_current_user)):
  updated_news = stadium.update_field(id, body.dict())

  if updated_news is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return updated_news.to_dict()


@router.delete("/{id}")
@roles_required(["admin"])
async def delete_field(id: str, user=Depends(get_current_user)):
  deleted_field = stadium.delete_field(id)
  if deleted_field is None:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Field not found")

  return HTTPException(status_code=status.HTTP_200_OK, detail="Delete field successfully")
