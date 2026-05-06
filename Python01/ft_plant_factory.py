class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print/Show the plant information"""
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def ft_plant_factory() -> None:
    """Create and display a registry of garden Plants."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end='')
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
