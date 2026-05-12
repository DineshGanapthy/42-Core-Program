class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def get_basic_info(self) -> str:
        """Print Basic Plant information"""
        return(f"=== {type(self).__name__}\n"
            f"{self.name}: {self.height:.1f}cm, {self.age} days old")

class Flower(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def updated_info(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print("Rose has not bloomed yet")
        print("[asking rose to bloom]")
        self.updated_info()
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}\n Color: {self.color}")
        self.bloom()

class Tree(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    #def updated_info(self) -> None:
    #   print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
    #   print(f" Color: {self.color}")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"{type(self).__name__} {self.name} now producing a shade of {self.height:.1f}cm long and {self.diameter:.1f}cm wide.\n")

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}\n Trunk diameter: {self.diameter:.1f}cm")
        self.produce_shade()

class Vegetable(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, 
                harvest_season: str, nutritional_value: int ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def harvest(self) -> None:
        print(f" Harvest season: {self.harvest_season}")

    def nutritional(self) -> None:
        print(f" Nutrition value: {self.nutritional_value}")

    def grow(self) -> None:
        self.age += 20
        self.nutritional_value += 20
        print(f"[make {self.name.lower()} grow and age for 20 days]")
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}")
        self.harvest()
        self.nutritional()
        self.grow()
        self.harvest()
        self.nutritional()
        #print()


def ft_plant_types() -> None:
    """Main Function"""
    garden = [
        Flower("Rose", 15, 10, "red"),
        Tree("Oak", 200, 365, 5),
        #Tree("Pine", 400, 1500, 40)
        Vegetable("Tomato", 5, 10, "April", 0),
        #Vegetable("Carrot", 30, 90, "August", 20)
    ]

    print("=== Garden Plant Types ===")
    for plant in garden:
        plant.get_info()


if __name__ == "__main__":
    ft_plant_types()