class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        """Print/Show the plant information"""
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self) -> None:
        """Increase the height by 0.8cm for each condition"""
        self.height += 0.8

    def age(self) -> None:
        """Increase the age by 1 day"""
        self.age_days += 1


def ft_plant_growth() -> None:
    """Create and display a registry of garden Plants."""

    current_day = 1
    plant = Plant("Rose", 25, 30)

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height
    while (current_day <= 7):
        print(f"=== Day {current_day} ===")
        plant.grow()
        plant.age()
        plant.show()
        current_day += 1
    final_height = plant.height
    print(f"Growth this week: {final_height - initial_height:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
