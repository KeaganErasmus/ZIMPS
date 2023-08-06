from GUI.cards import CardDeck
from GUI.tiles import TileDeck
from GUI.gui import GUI


class Game:
    """
    A single player game of Zombie in my pocket.
    """

    def __init__(self):
        self.gui = GUI()
        self.dev_cards = CardDeck(gui=self.gui)
        self.outdoor_tiles = TileDeck(deck_type='outdoor')
        self.indoor_tiles = TileDeck(deck_type='indoor')
        self.attack_score = 1
        self.health_score = 6
        self.time = '9 PM'
        self.player_location = (5, 3)
        self.player_inventory = []  # max 2 items
        self.board = {}
        self.patio_tile = None
        self.initialize_game()

    def initialize_game(self):
        # discard the first 2 development cards
        self.dev_cards.draw()
        self.dev_cards.draw()

        # Place the 'Foyer' tile on the board
        foyer_tile = self.indoor_tiles.draw_tile_by_name('Foyer')
        self.gui.place_tile(foyer_tile, 5, 3)
        self.board[(5, 3)] = foyer_tile

        # Set aside the 'Patio' tile
        self.patio_tile = self.outdoor_tiles.draw_tile_by_name('Patio')
        
        self.player_turn()
        

    def player_turn(self):
        current_tile = self.board[self.player_location]
        possible_exits = current_tile.get_possible_exits()
        print(
            f"You are in the {current_tile.name}. Possible exit directions: {possible_exits}")
        current_tile.display()
        chosen_exit = ""
        while chosen_exit not in possible_exits:
            chosen_exit = input("Choose a direction to exit: ").upper()
            if chosen_exit not in possible_exits:
                print(f"Invalid exit direction. Please choose a direction from: {possible_exits}")               
        
        self.player_location = self.update_location(chosen_exit)
        print(f"You chose to exit {chosen_exit}. Your new location is {self.player_location}.")
        # If the new location hasn't been explored, place a new tile
        if not self.is_explored(self.player_location):
            self.place_new_tile(chosen_exit)
        else:
            self.resolve_dev_card()
        
            
    def place_new_tile(self, chosen_exit):
        """
        Check if new tile has multiple exits(entries) and if so, ask the player to choose one side to enter from.
        Rotate the new tile accordingly.
        """
        new_tile = self.indoor_tiles.draw()
        possible_entries = new_tile.get_possible_exits()
        print(f"You found the {new_tile.name}, you can enter from the following sides: {possible_entries}")
        new_tile.display()
        chosen_entry = ""
        while chosen_entry not in possible_entries:
            chosen_entry = input("Choose a side to enter from: ").upper()
            if chosen_entry not in possible_entries:
                print(f"Invalid entry. Please choose from: {possible_entries}")

        print(f"You chose to enter from {chosen_entry}.")

        # Rotate new tile to align the chosen entry with the chosen exit from the previous tile
        new_tile = new_tile.rotate_tile_exits(chosen_entry, chosen_exit)
        new_tile.display()
        self.gui.place_tile(new_tile, *self.player_location)
        self.board[self.player_location] = new_tile
        self.resolve_dev_card()
        
        
    def resolve_dev_card(self):
        """
        Handle logic for resolving a development card.
        """
        if self.dev_cards.number_of_cards == 0:
            self.update_dev_deck_and_time()
            
        card = self.dev_cards.draw()
        card.display(self.time)
        card.image.show()
        self.player_turn()
    
    def is_explored(self, location):
        return location in self.board
    
    def update_dev_deck_and_time(self):
        """
        Create new development deck and update the time and discard the first 2 cards.
        """
        self.dev_cards = CardDeck(gui=self.gui)
        self.time = '10 PM' if self.time == '9 PM' else '11 PM'
        self.dev_cards.draw()
        self.dev_cards.draw()
        self.resolve_dev_card()

    
    def update_location(self, direction):
        x, y = self.player_location
        if direction == 'E':
            return x, y + 1
        elif direction == 'W':
            return x, y - 1
        elif direction == 'N':
            return x - 1, y
        elif direction == 'S':
            return x + 1, y

        
            