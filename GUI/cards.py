from PIL import Image
import random

IMAGE_PATH = 'assets/dev_cards.jpg'
CARDS = {
    '1': {'9 PM': {'text': 'You try hard not to wet yourself', 'value': 0}, '10 PM': {'text': 'ITEM', 'value': None}, '11 PM': {'text': 'zombies', 'value': 6}, 'Item': {'text': 'Oil', 'value': 0}},
    '2': {'9 PM': {'text': 'zombies', 'value': 4}, '10 PM': {'text': 'A bat poops in your eye', 'value': -1}, '11 PM': {'text': 'zombies', 'value': 6}, 'Item': {'text': 'Machete', 'value': 2}},
    '3': {'9 PM': {'text': 'zombies', 'value': 3}, '10 PM': {'text': 'You hear terrible screams', 'value': 0}, '11 PM': {'text': 'zombies', 'value': 5}, 'Item': {'text': 'Chainsaw', 'value': 3}},
    '4': {'9 PM': {'text': 'zombies', 'value': 4}, '10 PM': {'text': 'You sense your impending doom', 'value': -1}, '11 PM': {'text': 'ITEM', 'value': None}, 'Item': {'text': 'Gasoline', 'value': 0}},
    '5': {'9 PM': {'text': 'ITEM', 'value': None}, '10 PM': {'text': 'zombies', 'value': 5}, '11 PM': {'text': 'Your soul is not wanted here', 'value': -1}, 'Item': {'text': 'Grisly Femur', 'value': 1}},
    '6': {'9 PM': {'text': 'Candybar in your pocket', 'value': 1}, '10 PM': {'text': 'ITEM', 'value': None}, '11 PM': {'text': 'zombies', 'value': 4}, 'Item': {'text': 'Soda Can', 'value': 2}},
    '7': {'9 PM': {'text': 'ITEM', 'value': None}, '10 PM': {'text': 'zombies', 'value': 4}, '11 PM': {'text': 'Something icky in your mouth', 'value': -1}, 'Item': {'text': 'Board with Nails', 'value': 1}},
    '8': {'9 PM': {'text': 'Slipped on nasty goo', 'value': -1}, '10 PM': {'text': 'zombies', 'value': 4}, '11 PM': {'text': 'The smell of blood is in the air', 'value': 0}, 'Item': {'text': 'Golf Club', 'value': 1}},
    '9': {'9 PM': {'text': 'Your body shivers involuntarily', 'value': 0}, '10 PM': {'text': 'You feel a spark of hope', 'value': 1}, '11 PM': {'text': 'zombies', 'value': 4}, 'Item': {'text': 'Candle', 'value': 0}},
}


class Card:
    """
    A development card.
    """

    def __init__(self, image, content):
        self.image = image
        self.content = content


    def display(self, section_key='9 PM'):
        # self.image.show()
       # Print the content for the specified section of the card
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

    def __init__(self, image_path=IMAGE_PATH, cards_content=CARDS):
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
