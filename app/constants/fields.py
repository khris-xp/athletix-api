from ..internal.field import Field
from ..internal.slot_date import SlotDate

field1_slots1 = SlotDate(
    date="2023-04-15",
    start_time="09:00",
    end_time="10:00"
)

field1_slots1.set_is_booked(True)

field1_slots2 = SlotDate(
    date="2023-04-16",
    start_time="10:00",
    end_time="11:00"
)

field1_slots2.set_is_booked(True)

field1_slots3 = SlotDate(
    date="2023-04-16",
    start_time="11:00",
    end_time="12:00"
)

field1_slots3.set_is_booked(True)

football1_field = Field(
    name="Football Field 1",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="Football",
    type="Outdoor"
)

football1_field.add_slot(field1_slots1)
football1_field.add_slot(field1_slots2)
football1_field.add_slot(field1_slots3)

football2_field = Field(
    name="Football Field 2",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="Football",
    type="Outdoor"
)

football3_field = Field(
    name="Football Field 3",
    description="A standard football field with grass surface.",
    price_by_slot=300,
    category="Football",
    type="Indoor"
)

basketball1_field = Field(
    name="Basketball Field 1",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="Basketball",
    type="Indoor"
)

basketball2_field = Field(
    name="Basketball Field 2",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="Basketball",
    type="Indoor"
)

basketball3_field = Field(
    name="Basketball Field 3",
    description="A standard basketball field with concrete surface.",
    price_by_slot=300,
    category="Basketball",
    type="Outdoor"
)

badminton1_field = Field(
    name="Badminton Field 1",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="Indoor"
)

badminton2_field = Field(
    name="Badminton Field 2",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="Indoor"
)

badminton3_field = Field(
    name="Badminton Field 3",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="Indoor"
)
