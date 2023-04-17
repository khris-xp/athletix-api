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
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Football Field 1",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="football",
    type="outdoor"
)

football1_field.add_slot(field1_slots1)
football1_field.add_slot(field1_slots2)
football1_field.add_slot(field1_slots3)

football2_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Football Field 2",
    description="A standard football field with grass surface.",
    price_by_slot=500,
    category="football",
    type="outdoor"
)

football3_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Football Field 3",
    description="A standard football field with grass surface.",
    price_by_slot=300,
    category="football",
    type="indoor"
)

basketball1_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Basketball Field 1",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="basketball",
    type="indoor"
)

basketball2_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Basketball Field 2",
    description="A standard basketball field with concrete surface.",
    price_by_slot=500,
    category="basketball",
    type="indoor"
)

basketball3_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Basketball Field 3",
    description="A standard basketball field with concrete surface.",
    price_by_slot=300,
    category="basketball",
    type="outdoor"
)

badminton1_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Badminton Field 1",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="badminton",
    type="indoor"
)

badminton2_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Badminton Field 2",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="badminton",
    type="indoor"
)

badminton3_field = Field(
    image="https://editorial.uefa.com/resources/025c-0f8e775cc072-f99f8b3389ab-1000/the_new_tottenham_hotspur_stadium_has_an_unusual_flexible_playing_surface.jpeg",
    name="Badminton Field 3",
    description="A standard Badminton field with concrete surface.",
    price_by_slot=500,
    category="badminton",
    type="indoor"
)
