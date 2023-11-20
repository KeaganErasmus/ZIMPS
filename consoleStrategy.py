from abc import ABC, abstractmethod


class ActionStrategy(ABC):
    @abstractmethod
    def execute(self, game, args):
        pass


class GoStrategy(ActionStrategy):
    def execute(self, game, args):
        try:
            game.player_turn(args)
        except TypeError as err:
            print(str(err))


class BashStrategy(ActionStrategy):
    def execute(self, game, args):
        game.bash_through_wall(args)


class TotemStrategy(ActionStrategy):
    def execute(self, game, args):
        try:
            game.find_or_burry_totem()
        except TypeError as err:
            print(str(err))


class CowerStrategy(ActionStrategy):
    def execute(self, game, args):
        try:
            game.cower()
        except TypeError as err:
            print(str(err))


class QuitStrategy(ActionStrategy):
    def execute(self, game, args):
        print("Goodbye")
        game.gui.root.destroy()


class SaveStrategy(ActionStrategy):
    def execute(self, game, args):
        game.save_game()


class ShelveSaveStrategy(ActionStrategy):
    def execute(self, game, args):
        try:
            game.shelve_save(args)
        except:
            print("Please enter a filename to save to")


class ShelveLoadStrategy(ActionStrategy):
    def execute(self, game, args):
        game.shelve_load(args)


class JsonSaveStrategy(ActionStrategy):
    def execute(self, game, args):
        game.json_save(args)


class JsonLoadStrategy(ActionStrategy):
    def execute(self, game, args):
        game.json_load(args)


class LoadStrategy(ActionStrategy):
    def execute(self, game, args):
        game.load_game(args)


class DetailsStrategy(ActionStrategy):
    def execute(self, game, args):
        print(game.get_details())


class CoordsStrategy(ActionStrategy):
    def execute(self, game, args):
        print("  N\nW\tE\n  S")
