from PIL import ImageTk
import tkinter as tk

from cards import Deck


def show_card():
    card = deck.draw()
    card.print_content()

    card_image = card.image
    card_tk_image = ImageTk.PhotoImage(card_image)
    label_image.config(image=card_tk_image)
    label_image.image = card_tk_image

    # Update the label showing the number of cards remaining
    label_number_of_cards.config(
        text=f"Cards in Deck: {deck.get_number_of_cards()}")


# Create a deck of cards
deck = Deck('assets/dev_cards.jpg')

root = tk.Tk()
root.title("Card Drawer")

# Create a label to hold the card image
label_image = tk.Label(root)
label_image.pack()

# Create a label to show the number of cards
label_number_of_cards = tk.Label(
    root, text=f"Cards in Deck: {deck.get_number_of_cards()}")
label_number_of_cards.pack()

# Create a button to draw a new card
button_draw_card = tk.Button(root, text="Draw Card", command=show_card)
button_draw_card.pack()

# Start the GUI main loop
root.mainloop()
