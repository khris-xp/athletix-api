from fastapi import APIRouter, Depends, status, HTTPException
from ..utils.dependencies import get_current_user, role_required
from ..database.database import booking_history
from ..internal.booking import Booking
from ..internal.slot_date import SlotDate
from ..models.booking import BookingModel
from ..database.database import stadium, booking_history
from ..internal.payment import Payment

router = APIRouter(prefix="/booking",
                   tags=["booking"], responses={404: {"description": "Not found"}})


@router.post("/")
async def create_booking(body: BookingModel, user=Depends(get_current_user)):

  field_exist = stadium.get_field_by_id(body.field_id)

  if field_exist is None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Field not found")

  for equipment in body.equipments:
    equipment_exist = stadium.get_equipment_by_id(equipment['id'])
    if equipment_exist is None:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, detail="Equipment not found")
    elif equipment_exist.get_quantity() < equipment['quantity']:
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, detail="Equipment not enough")

  booked_slots = field_exist.get_booking_slots_by_date(body.slot['date'])

  for booked_slot in booked_slots:
    if booked_slot.is_equal(body.slot['start_time'], body.slot['end_time'], body.slot['date']):
      raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST, detail="Slot is booked")

  slot = SlotDate(start_time=body.slot['start_time'],
                  end_time=body.slot['end_time'], date=body.slot['date'])

  slot.set_is_booked(True)
  field_exist.add_slot(slot)

  price = field_exist.get_price_by_slot()

  for equipment in body.equipments:
    equipment_exist = stadium.get_equipment_by_id(equipment['id'])
    equipment_exist.set_quantity(
        equipment_exist.get_quantity() - equipment['quantity'])
    price += equipment_exist.get_price_per_unit() * equipment['quantity']

  new_payment = Payment(amount=price)
  new_booking = Booking(slot=slot, equipments=body.equipments,
                        customer_id=user.get_id(), field_id=body.field_id, payment=new_payment)

  booking_history.add_bookings(new_booking)

  return new_booking


@router.get("/")
@role_required("admin")
async def get_booking(user=Depends(get_current_user)):
  return booking_history.get_bookings()


@router.get("/history")
async def get_history(user=Depends(get_current_user)):
  return booking_history.get_booking_by_user(user.get_id())
