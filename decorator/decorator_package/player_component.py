from abc import ABC, abstractmethod


class PlayerComponent(ABC):
    @abstractmethod
    def get_details(self):
        """Executes the action in the context of the game."""
        pass
