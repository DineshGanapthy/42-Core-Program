class SecurePlant:
    def __init__(self, name: str) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self._height = 15
        self._age = 10

    def get_height(self) -> int:
        """Return Plant Height"""
        return self.__height

    def get_age(self) -> int:
        """Return Plant Age"""
        return self._age

    def set_height(self, height: int) -> None:
        """Set Plant Height"""
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        """Set Plant Age"""
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_info(self) -> str:
        """Print/Show Current State plant information"""
        return (f"{self.name}: {self._height:.1f}cm, {self._age} days old")


def ft_garden_security() -> None:
    """Main Function"""

    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print(f"Plant Created: {plant.get_info()}\n")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    plant.set_age(-35)
    print(f"\nCurrent state: {plant.get_info()}")


if __name__ == "__main__":
    ft_garden_security()
