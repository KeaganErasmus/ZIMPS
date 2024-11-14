from abc import ABC, abstractmethod

class ActionStrategy(ABC):
    @abstractmethod
    def execute(self, game, *args):
        """Executes the action in the context of the game."""
        pass
