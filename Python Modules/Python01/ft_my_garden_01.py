""" Ex0 """
# def ft_garden_intro() -> None:
#     name = "Rose"
#     height = 25
#     age = 30

#     print(
#         "=== Welcome to My Garden ===\n"
#         f"Plant: {name}\n"
#         f"Height: {height}cm\n"
#         f"Age: {age} days\n\n"
#         "=== End of the Program ==="
#     )

""" Ex1 """
# class Plant():
#     def __init__(self, name: str, height: int, age: int):
#         self.name = name
#         self.height = height
#         self.age = age

#     def show(self) -> None:
#         print(f"{self.name}: {self.height}cm, {self.age} days old")

# def ft_garden_data() -> None:
#     print("=== Garden Plant Registry ===")
#     rose = Plant("Rose", 25, 30)
#     sunflower = Plant("Sunflower", 80, 45)
#     cactus = Plant("Cactus", 15, 120)
#     rose.show()
#     sunflower.show()
#     catus.show()

""" Ex2 """
# class Plant():
#     def __init__(self, name: str, height: int, age: int, growth: int):
#         self.name = name
#         self.height = height
#         self.age = age
#         self.growth = growth

#     def show(self) -> None:
#         print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
    
#     def grow(self) -> None:
#         self.height += 0.8
#         self.growth += 0.8

#     def aging(self) -> None:
#         self.age += 1

# def ft_plant_growth() -> None:
#     print("=== Garden Plant Registry ===")
#     rose = Plant("Rose", 25, 30, 0)
#     rose.show()
#     days_of_week = 7

#     for i in range(days_of_week):
#         print(f"=== Day {i + 1} ===")
#         rose.grow()
#         rose.aging()
#         rose.show()
#     print(f"Growth this week: {rose.growth}cm")

""" Ex3 """
# class Plant():
#     def __init__(self, name: str, height: int, age: int):
#         self.name = name
#         self.height = height
#         self.age = age

#     def show(self) -> None:
#         print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

# def ft_plant_factory() -> None:
#     print("=== Plant Factory Output ===")
    
#     list_of_plants = [
#         Plant("Rose", 25, 30),
#         Plant("Oak", 200, 365),
#         Plant("Cactus", 5, 90),
#         Plant("Sunflower", 80, 45),
#         Plant("Fern", 15, 120),
#     ]
    
#     for plant in list_of_plants:
#         print("Created: ", end='')
#         plant.show()
#     """ Alternate way, add the "Created:" to the show method in the parent class
#         but by doing this you will be changing the method, although it does elimiate 
#         one lin eof code."""

""" Ex4 """
class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.updated_height = 0
        self.updated_age = 0

    # def set_height(self) -> None:
    #     get_height(self) == self.height

    def get_height(self) -> None:
        if (self.updated_height > 0):
            print(f"Height updated: {self.updated_height}cm")
            self.height = self.updated_height 
        else:
            print(f"{self.name}: Error, height can't be negative\n"
            "Height update rejected")
            #return (self.height)

    def get_age(self) -> None:
        if (self.updated_age > 0):
            print(f"Age updated: {self.updated_age} days\n")
        else:
            print(f"{self.name}: Error, age can't be negative\n"
            "Age update rejected\n")


    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    
    rose = Plant("Rose", 15, 10)
    rose.show()
    print()
    rose.updated_height = 25
    rose.updated_age = 30
    rose.get_height()
    rose.get_age()
    rose.updated_height = -25
    rose.updated_age = -35
    rose.get_height()
    rose.get_age()
    # rose.set_height()
    print("Current State: ", end='')
    rose.show()

    # list_of_plants = [
    #     Plant("Rose", 15, 10),
    #     Plant("Oak", 200, 365),
    #     Plant("Cactus", 5, 90),
    #     Plant("Sunflower", 80, 45)
    #     Plant("Fern", 15, 120),
    # ]

    rose.updated_height = 25
    
    # for plant in list_of_plants:
    #     print("Plant created: ", end='')
    #     plant.show()
    
if __name__ == "__main__":
    ft_garden_security()