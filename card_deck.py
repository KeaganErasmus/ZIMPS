# --------------------------------------------------------------
# card_deck.py
# --------------------------------------------------------------
# Author: Christian Diekmann
#
# Description:
# A deck of development cards represented as a Python class.
# Provides methods for initializing the deck from JSON and image files,
# shuffling, discarding, and drawing cards.
# ---------------------------------------------------------------
import json
import random
from PIL import Image, UnidentifiedImageError
from card import Card


class CardDeckInitializationError(Exception):
    pass


class CardDeck:
    """
    A deck of development cards.
    """

    def __init__(self, json_path, image_path):
        self.cards = []
        self.image_path = image_path
        cards_content = self._load_cards_content(json_path)
        if cards_content:
            self._initialize_cards(cards_content)
            self.shuffle_and_discard()

    def _load_cards_content(self, json_path):
        try:
            with open(json_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise CardDeckInitializationError(
                f"JSON file {json_path} not found.") from e
        except json.JSONDecodeError as e:
            raise CardDeckInitializationError(
                "JSON not valid for Development cards") from e

    def _initialize_cards(self, cards_content, rows=3, cols=3):
        try:
            image = Image.open(self.image_path)
        except FileNotFoundError as e:
            raise CardDeckInitializationError(
                f"Card image file {self.image_path} not found.") from e
        except UnidentifiedImageError as e:
            raise CardDeckInitializationError(
                f"Invalid card image for file {self.image_path}.") from e

        card_width, card_height = image.width // cols, image.height // rows
        for i in range(cols):
            for j in range(rows):
                left = i * card_width
                top = j * card_height
                right = (i + 1) * card_width
                bottom = (j + 1) * card_height
                card_image = image.crop((left, top, right, bottom))
                content = cards_content[i * rows + j]
                card = Card(card_image, content)
                self.cards.append(card)

    def shuffle_and_discard(self):
        """
        Shuffles the deck and discards the first 2 cards.
        """
        random.shuffle(self.cards)
        self.cards.pop(0)
        self.cards.pop(0)
        self.count = len(self.cards)

    def draw(self):
        """
        Draws a card from the deck.
        """
        if self.cards:
            card = self.cards.pop(0)  # Removes the top card from the deck
            self.count -= 1
            return card
