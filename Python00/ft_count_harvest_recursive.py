def ft_count_harvest_recursive() -> None:
    harvest_time = int(input('Days until harvest: '))
    starter = 1

    def countup(starter):
        if (harvest_time < starter):
            print("Harvest time")
        else:
            print("Day ", starter)
            countup(starter + 1)
    countup(starter)
