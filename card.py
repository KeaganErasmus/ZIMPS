class Card:
    """
    A development card.
    """

    def __init__(self, image, content):
        self.image = image
        self.content = content

    def display(self, section_key):
        """Displays the card's content.

        Args:
            section_key (str): The section of the card to display. eg '9 PM'
        """
        # self.image.show()
        print("Development Card:")
        print("---------------------------------------")
        print(section_key)
        section = self.content[section_key]
        text = section['text']
        value = section['value']
        if section_key == 'Item':
            print(f"{text}: {value}")
            return
        if text == 'zombies':
            print(f"{value} Zombies attack.. AHHH!!!")
        elif text == 'ITEM':
            print("You found an item: Draw another card to see what it is.")
        else:
            print(f"{text}")
        print("---------------------------------------")
