from ..internal.basketball import BasketBall
from ..internal.football import FootBall
from ..internal.shuttlecock import ShuttleCock
from ..internal.vest import Vest


football_equipment = FootBall(
    name="football",
    price_per_unit=0,
    quantity=10,
    category="football"
)

basketball_equipment = BasketBall(
    name="basketball",
    price_per_unit=0,
    quantity=10,
    category="basketball"
)

shuttlecock_equipment = ShuttleCock(
    name="shuttlecock",
    price_per_unit=0,
    quantity=10,
    category="badminton"
)

vest_equipment = Vest(
    name="vest",
    price_per_unit=0,
    quantity=30,
    category="all"
)
