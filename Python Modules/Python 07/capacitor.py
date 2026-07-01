from ex1 import HealingCreatureFactory, TransformCreatureFactory

def testing_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal() + "\n")

def testing_transforing(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base1 = factory.create_base()
    evolved1 = factory.create_evolved()
    print(base1.describe())
    print(base1.attack())
    print(base1.transform())
    print(base1.attack())
    print(base1.revert())
    print(" evolved:")
    print(evolved1.describe())
    print(evolved1.attack())
    print(evolved1.transform())
    print(evolved1.attack())
    print(evolved1.revert())

if __name__ == "__main__":
    testing_healing(HealingCreatureFactory())
    testing_transforing(TransformCreatureFactory())