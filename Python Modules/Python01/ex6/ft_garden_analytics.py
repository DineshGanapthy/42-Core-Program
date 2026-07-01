class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age
    
    @staticmethod
    def check_age(age: int):
        if age > 365:
            print(f"Is {age} days more then a year ? -> True")
            return (True)
        else:
            print(f"Is {age} days more then a year ? -> False")
            return (False)
            
    def get_basic_info(self) -> str:
        """Print Basic Plant information"""
        return(f"=== {type(self).__name__}\n"
            f"{self.name}: {self.height:.1f}cm, {self.age} days old")

class Flower(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, color: str, grow_call: int, age_call: int, show_count: int) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.grow_call = grow_call
        self.age_call = age_call
        self.show_count = show_count

    def show_stats(self):
        self.show_count += 1
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_count} show")

    def grow(self) -> None:
        self.height += 8
        self.grow_call += 1

    def updated_info(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print(" Rose has not bloomed yet")
        self.show_stats()
        print("[asking rose to grow and bloom]")
        self.grow()
        self.updated_info()
        print(f" {self.name} is blooming beautifully!")
        self.show_stats()

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}\n Color: {self.color}")
        self.bloom()
        print()

class Tree(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, diameter: int, grow_call: int, age_call: int, show_count: int, shade: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter
        self.grow_call = grow_call
        self.age_call = age_call
        self.show_count = show_count
        self.shade = shade

    def show_stats(self):
        #self.show_count += 1
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_count} show\n{self.shade} shade")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"{type(self).__name__} {self.name} now producing a shade of {self.height:.1f}cm long and {self.diameter:.1f}cm wide.")
        self.shade += 1

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}\n Trunk diameter: {self.diameter:.1f}cm")
        self.show_stats()
        self.produce_shade()
        self.show_stats()
        print()

class Seed(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, color: str, grow_call: int, age_call: int, show_count: int, seed: int) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.seed = seed
        self.grow_call = grow_call
        self.age_call = age_call
        self.show_count = show_count

    def show_stats(self):
        self.show_count += 1
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_count} show")

    def grow(self) -> None:
        self.height += 30
        self.age += 20
        self.seed += 42
        self.grow_call += 1
        self.age_call += 1

    def seed_grow(self) -> None :
        seed += 42

    def show_seed(self) -> None:
        print(f"Seeds : {self.seed}")

    def updated_info(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print(f" {self.name} has not bloomed yet")
        self.show_seed()
        print(f"[make {self.name.lower()} grow, age and bloom]")
        #self.show_stats()
        self.grow()
        self.updated_info()
        print(f" {self.name} is blooming beautifully!")
        self.show_seed()
        self.show_stats()
        #self.show_grow()

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}\n Color: {self.color}")
        self.bloom()
        print()

class Anonymous(Plant):
    """Initialize a Plant Subclass"""
    def __init__(self, name: str, height: int, age: int, grow_call: int, age_call: int, show_count: int) -> None:
        super().__init__(name, height, age)
        self.grow_call = grow_call
        self.age_call = age_call
        self.show_count = show_count

    def show_stats(self):
        self.show_count += 1
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_count} show")

    def grow(self) -> None:
        self.age_call += 1

    def updated_info(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def get_info(self) -> None:
        print(f"{self.get_basic_info()}")
        self.show_stats()


def ft_garden_analytics() -> None:
    """Main Function"""
    garden = [
        Flower("Rose", 15, 10, "red", 0 , 0, 0),
        Tree("Oak", 200, 365, 5, 0 ,0 ,1, 0),
        Seed("Sunflower", 80, 45, "yellow", 0 ,0 ,1, 0),
        Anonymous("Unknown plant", 0, 0, 0, 0, 0),
        #Vegetable("Carrot", 30, 90, "August", 20)
    ]

    print("=== Garden Plant Types ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print()
    for plant in garden:
        plant.get_info()


if __name__ == "__main__":
    ft_garden_analytics()