from PIL import Image
import random

SECTIONS = ["9 PM", "10 PM", "11 PM", "Item"]
CARDS = {
    '1': [{'You try hard not to wet yourself': 0}, {'ITEM': None}, {'zombies': 6}, {'Oil': 0}],
    '2': [{'zombies': 4}, {'A bat poops in your eye': -1}, {'zombies': 6}, {'Machete': 2}],
    '3': [{'zombies': 3}, {'You hear terrible screams': 0}, {'zombies': 5}, {'Chainsaw': 3}],
    '4': [{'zombies': 4}, {'You sense your impending doom': -1}, {'ITEM': None}, {'Gasoline': 0}],
    '5': [{'ITEM': None}, {'zombies': 5}, {'Your soul is not wanted here': -1}, {'Grisly Femur': 1}],
    '6': [{'Candybar in your pocket': 1}, {'ITEM': None}, {'zombies': 4}, {'Soda Can': 2}],
    '7': [{'ITEM': None}, {'zombies': 4}, {'Something icky in your mouth': -1}, {'Board with Nails': 1}],
    '8': [{'Slipped on nasty goo': -1}, {'zombies': 4}, {'The smell of blood is in the air': 0}, {'Golf Club': 1}],
    '9': [{'Your body shivers involuntarily': 0}, {'You feel a spark of hope': 1}, {'zombies': 4}, {'Candle': 0}],
}


class Card:
    """
    A development card.
    """

    def __init__(self, image, content):
        self.image = image
        self.content = content

    def show(self):
        self.image.show()

    def print_content(self):
        # Iterate through the cards sections and print based on the key
        print("Card Content:")
        print("---------------")
        for i, section in enumerate(self.content):
            print(SECTIONS[i])
            for key, value in section.items():
                if key == 'zombies':
                    print(f"{value} Zombies")
                elif key == 'ITEM':
                    print("ITEM")
                else:
                    print(f"{key}: {value}")
        print("---------------")


class DevelopmentDeck:
    """
    A deck of development cards.
    """

    def __init__(self, image_path, cards_content=CARDS):
        self.cards = []
        image = Image.open(image_path)
        card_width, card_height = image.width // 3, image.height // 3

        card_index = 1
        # Iterate through the image and create a card for each section of the 3x3 grid
        for i in range(3):
            for j in range(3):
                left = i * card_width
                top = j * card_height
                right = (i + 1) * card_width
                bottom = (j + 1) * card_height
                print(left, top, right, bottom)
                card_image = image.crop((left, top, right, bottom))
                # Get the contents for this card
                content = cards_content[str(card_index)]
                card = Card(card_image, content)
                self.cards.append(card)
                card_index += 1

        random.shuffle(self.cards)
        self.number_of_cards = len(self.cards)

    def draw(self):
        if self.cards:
            card = self.cards.pop(0)  # Removes the top card from the deck
            self.number_of_cards -= 1
            return card

    def get_number_of_cards(self):
        return self.number_of_cards

    def show_top(self):
        if self.cards:
            self.cards[0].show()
