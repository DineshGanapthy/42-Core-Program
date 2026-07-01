#absolute path
import elements
from alchemy.potions import strength_potion

#relative path
from ..elements import create_air

def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: "
            f"brew' {create_air()}' and '{strength_potion()}'" 
            f"mixed with '{elements.create_fire()}'")
