from ex0 import FlameFactory, AquaFactory
# from ex0.Factories import CreatureFactory

def testing_factory(factory: CreatureFactory) -> None:
    print("Testing Factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack() + "\n")

def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()
    print(f"{base1.describe()}\n vs. \n{base2.describe()}")
    print(" fight!")
    print(base1.attack())
    print(base2.attack())

if __name__ == "__main__":
    testing_factory(FlameFactory())
    testing_factory(AquaFactory())
    battle(FlameFactory(), AquaFactory())
