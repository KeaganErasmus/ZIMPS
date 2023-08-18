class Player:
    def __init__(self, x, y, health, attack, items, has_totem, score, game):
        self.x = x
        self.y = y
        self.health = health
        self.attack = attack
        self.items = items
        self.has_totem = has_totem
        self.score = score
        self.game = game

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_items(self):
        return self.items

    def get_health(self):
        return self.health

    def take_damage(self, amount):
        self.health -= amount

    def take_totem(self):
        self.has_totem = True

    def get_details(self):
        return f'Current location: x->{self.x}, y->{self.y} \nhealth->{self.health}'