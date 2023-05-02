from fastapi import APIRouter, Depends, status, HTTPException
from ..utils.dependencies import get_current_user, roles_required
from ..internal.booking import Booking
from ..internal.slot_date import SlotDate
from ..models.booking import BookingModel, ApproveBookingModel, CancelBookingModel
from ..database.database import stadium
from ..internal.cash_payment import CashPayment
from ..internal.promptpay_payment import PromptPayPayment

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

  if body.payment_method == "cash":
    new_payment = CashPayment(amount=price)
  elif body.payment_method == "promptpay":
    new_payment = PromptPayPayment(amount=price)
  else:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid")

  equipments = [
      {
          "id": equipment['id'],
          "quantity": equipment['quantity'],
          "name": stadium.get_equipment_by_id(equipment['id']).get_name(),
      }
      for equipment in body.equipments
  ]

  new_booking = Booking(slot=slot, equipments=equipments,
                        customer={"id": user.get_id(), "fullname": user.get_fullname()}, field={
                            "id": field_exist.get_id(), "name": field_exist.get_name()}, payment=new_payment)

  stadium.add_booking(new_booking)

  return new_booking.to_dict()


@router.get("/")
@roles_required(["admin"])
async def get_booking(user=Depends(get_current_user)):
  return [booking.to_dict() for booking in stadium.get_bookings()]


@router.get("/history")
async def get_history(user=Depends(get_current_user)):
  return [booking.to_dict() for booking in stadium.get_bookings_by_user(user.get_id())]


@router.post("/approve")
@roles_required(["frontdesk", "admin"])
async def approve_booking(body: ApproveBookingModel, user=Depends(get_current_user)):
  booking_exist = stadium.get_booking_by_id(body.booking_id)

  if booking_exist is None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Booking not found")

  if booking_exist.get_payment().get_is_payed() == False:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Not pay yet")

  booking_exist.set_status("success")

  return {"message": "Approve successfully"}


@router.delete("/{booking_id}")
async def delete_booking(booking_id: str, user=Depends(get_current_user)):
  booking_exist = stadium.get_booking_by_id(booking_id)

  if booking_exist is None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Booking not found")

  stadium.delete_booking(booking_id)

  return {"message": "Delete successfully"}
