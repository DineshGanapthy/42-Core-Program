class GardenError(Exception):
    """Base exception for garden-related errors"""
    pass


class PlantError(GardenError):
    """Raise when a plant-related error occurs"""
    pass


class WaterError(GardenError):
    """Raised when a watering error occurs"""
    pass


def plant_error(plant_name: str, health: int) -> None:
    """Creates a plant error message"""
    if health < 5:
        raise PlantError(f"The {plant_name} plant is wilting!")


def water_error(water_amount: int) -> None:
    """Creates a water error message"""
    if water_amount < 5:
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    """Tests on different error types"""
    print("=== Custom Garden Error Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_error("tomato", 1)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_error(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        plant_error("tomato", 1)
    except PlantError as e:
        print(f"Caught WaterError: {e}")
    try:
        water_error(3)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("All customs errors types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
