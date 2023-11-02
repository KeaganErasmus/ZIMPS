class Player:
    def __init__(self, start_coordinates, health=6, attack=1, items=None):
        self.location = start_coordinates
        self.health = health
        self.attack = attack
        self.items = items
        if self.items is None:
            self.items = []
        self.has_totem = False

    def get_location(self):
        return self.location

    def get_attack(self):
        return self.attack

    def get_items(self):
        return self.items

    def get_health(self):
        return self.health

    def take_damage(self, amount):
        self.health -= amount

    def take_totem(self):
        self.has_totem = True

    def get_details(self):
        return (f'Location->{self.location} '
                f'\nHealth->{self.health} '
                f'\nAttack->{self.attack} '
                f'\nItems->{self.items}'
                f'\nTotem->{self.has_totem}')
