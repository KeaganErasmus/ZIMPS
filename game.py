from board import Board
from player import Player
from GUI.gui import GUI


class Game:
    """
    The Game class controls the game logic eg (movement, attack)
    """

    def __init__(self, start_coordinates=(5, 3)):
        self.player = Player(start_coordinates)
        self.board = Board(start_coordinates)
        self.gui = GUI()
        self._setup(start_coordinates)

    def _setup(self, start_coordinates):
        self.gui.place_tile(self.board.foyer_tile, *start_coordinates)
        self._update_gui_labels()
        self._print_current_room()

    def _update_gui_labels(self):
        self.gui.update_dev_cards(self.board.dev_cards.count, self.board.time)
        self.gui.update_tile_count(
            self.board.indoor_tiles.count, self.board.outdoor_tiles.count)
        self.gui.update_player_info(
            self.player.health, self.player.attack, self.player.items)

    def _print_current_room(self):
        print(f"You are in the {self._current_room().name}.")
        print(f"Possible directions: {self._current_room().possible_exits()}")
        self._current_room().display()

    def _current_room(self):
        return self.board.tile_map[self.player.location]

    def player_turn(self, direction):
        possible_exits = self._current_room().possible_exits()
        if direction not in possible_exits:
            print(
                f"Invalid exit direction. Choose from: {possible_exits}")
            return

        new_location = self.update_location(direction)
        if self.board.is_explored(new_location):
            room = self.board.tile_map[new_location]
            if self.opposite_direction(direction) not in room.possible_exits():
                print("This exit is blocked by a wall from another room.")
                return

            self.player.location = new_location
            self.resolve_dev_card(room)
        else:
            self.player.location = new_location
            self._place_new_tile(direction)

    def _place_new_tile(self, chosen_exit):
        """
        Choose side to enter new room from.
        Rotate the new tile accordingly.
        """
        # TODO:
        # logic to draw from correct tile deck (outdoor/indoor)
        # logic to place patio tile when moving outside
        new_tile = self.board.indoor_tiles.draw()
        self.gui.place_tile(new_tile, *self.player.location)

        possible_entries = new_tile.possible_exits()
        if new_tile.name == 'Dining Room':
            # 'N' is reserved for exit to the Patio
            possible_entries.remove('N')
        if len(possible_entries) > 1:
            new_tile = self._choose_entry(
                chosen_exit, new_tile, possible_entries)
        else:
            new_tile = new_tile.rotate_tile(
                possible_entries[0], chosen_exit)

        self.gui.place_tile(new_tile, *self.player.location)
        self.board.tile_map[self.player.location] = new_tile
        self.resolve_dev_card(new_tile)

    def _choose_entry(self, chosen_exit, new_tile, possible_entries):
        print(
            f"You found the {new_tile.name}, you can enter from: {possible_entries}")
        chosen_entry = ""
        while chosen_entry not in possible_entries:
            chosen_entry = input("Choose a side to enter from: ").upper()
            if chosen_entry not in possible_entries:
                print(f"Invalid entry. Please choose from: {possible_entries}")

        return new_tile.rotate_tile(chosen_entry, chosen_exit)

    def resolve_dev_card(self, room):
        """
        Handle logic for resolving a development card.
        """
        room.display()
        card = self.board.dev_cards.draw()
        card.display(self.board.time)
        # TODO: implement card logic
        return

    def _game_over(self):
        """
        Check if the game is over.
        """
        if self.board.dev_cards.number_of_cards == 0:
            if self.board.time == "11 PM":
                print("You ran out of time. GAME OVER!")
                return True
            self.board.update_time()

            return True
        return False

    def _opposite_direction(direction):
        opposites = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        return opposites.get(direction, "Invalid direction")

    def _update_location(self, direction):
        """
        Update the player location based on the chosen exit direction.
        """
        x, y = self.player.location
        if direction == 'E':
            return x, y + 1
        elif direction == 'W':
            return x, y - 1
        elif direction == 'N':
            return x - 1, y
        elif direction == 'S':
            return x + 1, y
