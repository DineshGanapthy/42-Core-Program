def ft_count_harvest_iterative() -> None:
    harvest_time = int(input('Days until harvest: '))
    for i in range(harvest_time):
        print("Day", i + 1)
    print("Harvest time!")
