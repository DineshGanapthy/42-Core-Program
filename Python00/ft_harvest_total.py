def ft_harvest_total() -> None:
    day_1 = input('Day 1 harvest :')
    day_2 = input('Day 2 harvest :')
    day_3 = input('Day 3 harvest :')
    weight = int(day_1) + int(day_2) + int(day_3)
    print("Total harvest :", weight)
