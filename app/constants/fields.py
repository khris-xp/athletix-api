from ..internal.field import Field
from ..internal.slot_date import SlotDate

field1_slots1 = SlotDate(
    date="2023-04-20T00:00:00.000Z",
    start_time="2023-04-20T09:00:00.000Z",
    end_time="2023-04-20T10:00:00.000Z"
)

field1_slots1.set_is_booked(True)

field1_slots2 = SlotDate(
    date="2023-04-21T00:00:00.000Z",
    start_time="2023-04-21T09:00:00.000Z",
    end_time="2023-04-21T10:00:00.000Z"
)

field1_slots2.set_is_booked(True)

field1_slots3 = SlotDate(
    date="2023-04-21T00:00:00.000Z",
    start_time="2023-04-21T11:00:00.000Z",
    end_time="2023-04-21T12:00:00.000Z"
)

field1_slots3.set_is_booked(True)

football1_field = Field(
    name="Football Field 1",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="Football",
    type="outdoor"
)

football1_field.add_slot(field1_slots1)
football1_field.add_slot(field1_slots2)
football1_field.add_slot(field1_slots3)

football2_field = Field(
    name="Football Field 2",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="Football",
    type="outdoor"
)

football3_field = Field(
    name="Football Field 3",
    description="A standard football field with grass surface.",
    price_by_slot=300,
    category="Football",
    type="indoor"
)

basketball1_field = Field(
    name="Basketball Field 1",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="Basketball",
    type="indoor"
)

basketball2_field = Field(
    name="Basketball Field 2",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="Basketball",
    type="indoor"
)

basketball3_field = Field(
    name="Basketball Field 3",
    description="A standard basketball field with concrete surface.",
    price_by_slot=300,
    category="Basketball",
    type="outdoor"
)

badminton1_field = Field(
    name="Badminton Field 1",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="indoor"
)

badminton2_field = Field(
    name="Badminton Field 2",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="indoor"
)

badminton3_field = Field(
    name="Badminton Field 3",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="Badminton",
    type="indoor"
)
