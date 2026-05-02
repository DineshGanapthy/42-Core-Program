def ft_water_reminder() -> None:
    water_remainder = int(input('Days since last watering : '))
    if (water_remainder > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
