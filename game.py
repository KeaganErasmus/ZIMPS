import pickle

from board import Board
from player import Player
from GUI.gui import GUI
from pickling import Pickling


class Game:
    """
    The Game class controls the game logic eg (movement, attack)
    """

    def __init__(self, start_coordinates=(5, 3)):
        self.player = Player(start_coordinates)
        self.board = Board(start_coordinates)
        self.gui = GUI()
        self.pickle = Pickling()
        self._setup(start_coordinates)

    def save_game(self):
        self.pickle.dump_file(self.player)
        print(f"Saving file")

    def load_game(self, filename):
        try:
            file = self.pickle.load_file()
            for line in file:
                print(line.get_details())
        except EOFError:
            return print("There is no file to load")


    def get_details(self):
        self.player.get_details()

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

    def _move_direction(self, direction):
        possible_exits = self._current_room().possible_exits()
        if direction not in possible_exits:
            print(
                f"Invalid direction. Choose from: {possible_exits}")
            return
        return self._update_location(direction)

    def player_turn(self, direction):
        direction = direction.upper()
        new_location = self._move_direction(direction)
        if self.board.is_explored(new_location):
            room = self.board.tile_map[new_location]
            if self._opposite_direction(direction) not in room.possible_exits():
                print("This exit is blocked by a wall from another room.")
                return
            self.player.location = new_location
            self._resolve_dev_card(room)
        else:
            new_tile, tile_type = self.board.draw_tile(self._current_room())
            if new_tile is None:
                print(f"No more {tile_type} tiles to draw.")
                return
            self.player.location = new_location
            self.gui.place_tile(new_tile, *new_location)
            self._place_new_tile(direction, new_tile)

        self.save_game()

    def _place_new_tile(self, chosen_exit, new_tile):
        """
        Choose side to enter new room from.
        Rotate the new tile accordingly.
        """
        # TODO:
        # logic to place patio tile when moving outside
        # logic to bash down wall if no other exits
        possible_entries = new_tile.possible_exits()
        if len(possible_entries) > 1:
            new_tile = self._choose_entry(
                chosen_exit, new_tile, possible_entries)
        else:
            new_tile = new_tile.rotate(
                possible_entries[0], chosen_exit)

        self.gui.place_tile(new_tile, *self.player.location)
        self.board.tile_map[self.player.location] = new_tile
        self._resolve_dev_card(new_tile)

    def _choose_entry(self, chosen_exit, new_tile, possible_entries):
        if new_tile.name == 'Dining Room':
            # 'N' is reserved for exit to the Patio
            possible_entries.remove('N')
            # place patio tile with 'N' to (N) of Dining room
        print(
            f"You found the {new_tile.name}, you can enter from: {possible_entries}")
        chosen_entry = ""
        while chosen_entry not in possible_entries:
            chosen_entry = input("Choose a side to enter from: ").upper()
            if chosen_entry not in possible_entries:
                print(f"Invalid entry. Please choose from: {possible_entries}")

        # if new_tile.name == 'Dining Room':
        #     patio_tile = self.board.patio_tile.rotate(
        #         'N', self._opposite_direction(chosen_entry))  # not tested
        #     patio_location = self._update_location('N')
        #     self.board.tile_map[patio_location] = patio_tile
        #     self.gui.place_tile(patio_tile, *patio_location)

        return new_tile.rotate(chosen_entry, chosen_exit)

    def _resolve_dev_card(self, tile):
        """
        Handle logic for resolving a development card.
        """
        card = self.board.dev_cards.draw()
        card.display(self.board.time)
        content = card.content[self.board.time]
        if content['text'] == 'zombies':
            self._runaway_or_fight(content['value'])
        elif content['text'] == 'ITEM':
            self._get_new_item()
        else:
            self.player.health += content['value']

        if not self._game_over():
            if tile.name == 'Kitchen' or tile.name == 'Garden':
                self.player.health += 1
            elif tile.name == 'Storage':
                self._get_new_item()

        self._update_gui_labels()
        return

    def _runaway_or_fight(self, num_zombies):
        """
        handle logic for running away or fighting
        """
        possible_actions = ['F', 'R']
        print("Enter 'F' to fight or 'R' to run away.")
        action = ""
        while action not in possible_actions:
            action = input("Choose your action: ").upper()
            if action not in possible_actions:
                print(f"Invalid, choose: {possible_actions}")

        if action == 'R':
            self._escape_zombies()

        if action == 'F':
            damage = num_zombies - self.player.attack
            if damage >= 0:
                self.player.take_damage(damage)
                self.player.attack = 0
            else:  # no damage only decrease attack
                self.player.attack += damage
        return

    def _escape_zombies(self):
        # logic to only run into previously explored rooms
        self.player.health -= 1

    def _get_new_item(self):
        """
        Logic for getting new items
        """
        possible_actions = ["Y", "N"]
        action = ""
        if not self._game_over():
            new_item = self.board.dev_cards.draw().content['Item']
            item_name = new_item['text']
            item_value = new_item['value']
            print(f"You found {item_name}")

            self.remove_items(action, item_name, possible_actions)

    def remove_items(self, action, item_name, possible_actions):
        """
        This function does the logic for replacing items
        if the player wants to
        """
        if len(self.player.items) >= 2:
            while action not in possible_actions:
                action = input("Do you want to replace one of your items? (Y/N): ").upper()
                print(f"Your current items: {self.player.items}")
                if action not in possible_actions:
                    print(f"Invalid choice, choose: {possible_actions}")

            if action == "Y":
                item_to_replace = input("Choose an item to replace: ")
                if item_to_replace in self.player.items:
                    self.player.items.remove(item_to_replace)
                    self.player.items.append(item_name)
                    print(f"You replaced {item_to_replace} with {item_name}.")
                else:
                    print("Invalid item choice.")
        else:
            self.player.items.append(item_name)

    def cower(self):
        self.player.health += 3
        self.board.dev_cards.draw()
        self._update_gui_labels()
        if not self._game_over():
            self._print_current_room()
        return

    def _game_over(self):
        """
        Check if the game is over.
        """
        if self.board.dev_cards.count == 0:
            if self.board.time == "11 PM":
                print("You ran out of time. GAME OVER!")
                return True
            self.board.update_time()

        if self.player.health == 0:
            print("You died. GAME OVER!")
            return True

        self._update_gui_labels()
        return False

    def _opposite_direction(self, direction):
        opposites = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        return opposites.get(direction, "Invalid direction")

    def _update_location(self, direction):
        """
        Calculate the new location based on the chosen exit direction.
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
