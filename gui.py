from PIL import ImageTk, Image
import tkinter as tk

from cards import DevelopmentDeck


class GUI:
    """
    A GUI for drawing cards from a deck.
    """

    def __init__(self):
        self.dev_deck = DevelopmentDeck('assets/dev_cards.jpg')

        self.root = tk.Tk()
        self.root.title("Zombie in my pocket")

        # Create a blank placeholder image
        self.placeholder_image = Image.new('RGB', (345, 517), color='white')
        self.placeholder_tk_image = ImageTk.PhotoImage(self.placeholder_image)

        # Create a label to hold the card image and set the placeholder as the initial image
        self.label_image = tk.Label(self.root, image=self.placeholder_tk_image)
        self.label_image.image = self.placeholder_tk_image  # keep a reference
        self.label_image.pack()

        # Create a label to show the number of cards
        self.label_number_of_cards = tk.Label(
            self.root, text=f"Development Cards: {self.dev_deck.get_number_of_cards()}")
        self.label_number_of_cards.pack()

        # Create a button to draw a new card
        self.button_draw_card = tk.Button(
            self.root, text="Draw Development Card", command=self.draw_dev_card)
        self.button_draw_card.pack()

        # Start the GUI main loop
        self.root.mainloop()

    def draw_dev_card(self):
        card = self.dev_deck.draw()
        card.print_content()

        card_image = card.image
        card_tk_image = ImageTk.PhotoImage(card_image)
        self.label_image.config(image=card_tk_image)
        self.label_image.image = card_tk_image

        # Update the label showing the number of cards remaining
        self.label_number_of_cards.config(
            text=f"Development Cards: {self.dev_deck.get_number_of_cards()}")


# Create and run the GUI
app = GUI()
