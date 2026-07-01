from abc import ABC,abstractmethod
from ex0.Creature import Creature
from ex1.Capabilities import TransformCapability, HealCapability

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True 

    def act(self, creature: Creature) -> list:
        return [creature.attack()]

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list:
        if self.is_valid(creature) == False:
            raise InvaildStrategyError(
                f"Invalid Creature {creature.name} for this"
                "aggresive strategy"
            )
        else:
            return [
                creature.transform(),
                creature.attack(),
                creature.revert()
            ]
    
class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list:
        if self.is_valid(creature) == False:
            raise InvaildStrategyError(
                f"Invalid Creature {creature.name} for this"
                "defensive strategy"
            )
        else:
            return [
                creature.attack(),
                creature.heal()
            ]


        

