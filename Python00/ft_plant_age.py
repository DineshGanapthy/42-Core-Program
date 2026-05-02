def ft_plant_age() -> None:
    plant_age = input('Enter plant age in days : ')
    if (int(plant_age) > 60):
        print("Plant is ready to harvest!")
    elif (int(plant_age) < 60):
        print("Plant needs more time to grow")
