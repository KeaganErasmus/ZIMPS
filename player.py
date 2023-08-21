class Player:
    def __init__(self, start_coordinates, health=6, attack=1, has_totem=False):
        self.location = start_coordinates
        self.health = health
        self.attack = attack
        self.items = []
        self.has_totem = has_totem

    def get_location(self):
        return self.location

    def get_items(self):
        return self.items

    def get_health(self):
        return self.health

    def take_damage(self, amount):
        self.health -= amount

    def take_totem(self):
        self.has_totem = True

    def get_details(self):
        return print(f'Location->{self.location} \nHealth->{self.health} \nAttack->{self.attack} \nItems->{self.items}')
