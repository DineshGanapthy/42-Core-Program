class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name  # these are the objects we are creating in the class.
        self.height = height
        self.age = age

    def show(self) -> None:
        """Print/Show the plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    """Create and display a registry of garden Plants."""
    rose = Plant("Rose", 25, 30)  # object1
    sunflower = Plant("Sunflower", 80, 45)  # object2
    cactus = Plant("Cactus", 15, 120)  # object3

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()

# def ft_garden_data() -> None:
# 	"""Create and display a registry of garden Plants."""
# Here I created one object, a list called plants,
# in the list i have three item
# the subject asks for
# three seperate objects
#
# 	plants = [
# 		Plant("Rose", 25, 30),
# 		Plant("Sunflower", 80, 45),
# 		Plant("Cactus", 15, 120),
# 	]
# 	print("=== Garden Plant Registry ===")
# 	for plant in plants:
# 		plant.show()
