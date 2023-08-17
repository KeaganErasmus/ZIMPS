from PIL import Image
import random
import json

IMAGE_PATH = 'assets/dev_cards.jpg'
JSON_PATH = 'assets/dev_cards.json'


class Card:
    """
    A development card.
    """

    def __init__(self, image, content):
        self.image = image
        self.content = content

    def display(self, section_key='9 PM'):
        """Prints the cards content to the console.

        Args:
            section_key (str, optional): The section(time) of the card to display. Defaults to '9 PM'.
        """
        # self.image.show()
        print("Development Card:")
        print("------------------------------")
        print(section_key)
        section = self.content[section_key]
        text = section['text']
        value = section['value']
        if section_key == 'Item':
            print(f"{text}: {value}")
            return
        if text == 'zombies':
            print(f"{value} Zombies")
        elif text == 'ITEM':
            print("ITEM: Draw another card and keep the item on it.")
        else:
            print(f"{text}: {value}")
        print("------------------------------")


class CardDeck:
    """
    A deck of development cards.
    """

    def __init__(self, image_path=IMAGE_PATH, json_path=JSON_PATH):
        self.cards = []
        self.image_path = image_path
        cards_content = self.load_cards_content(json_path)
        if cards_content:
            self.initialize_cards(cards_content)
            self.shuffle_and_discard()

    def load_cards_content(self, json_path):
        try:
            with open(json_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {json_path} not found. Loading cards failed.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {json_path}. Loading cards failed.")
            return None

    def initialize_cards(self, cards_content):
        image = Image.open(self.image_path)
        card_width, card_height = image.width // 3, image.height // 3
        for i in range(3):
            for j in range(3):
                left = i * card_width
                top = j * card_height
                right = (i + 1) * card_width
                bottom = (j + 1) * card_height
                card_image = image.crop((left, top, right, bottom))
                content = cards_content[i * 3 + j]
                card = Card(card_image, content)
                self.cards.append(card)

    def shuffle_and_discard(self):
        random.shuffle(self.cards)
        self.cards.pop(0)  # discard the first 2 cards
        self.cards.pop(0)
        self.number_of_cards = len(self.cards)

    def draw(self):
        if self.cards:
            card = self.cards.pop(0)  # Removes the top card from the deck
            self.number_of_cards -= 1
            return card
