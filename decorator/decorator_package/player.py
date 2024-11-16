from decorator_package import PlayerComponent


class Player(PlayerComponent):
    def __init__(self,
                 start_coordinates,
                 health=6,
                 attack=1,
                 items=None,
                 has_totem=False):
        self.location = start_coordinates
        self.health = health
        self.attack = attack
        self.items = items if items else []
        self.has_totem = has_totem

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
        return (
            f"Location->{self.location} \n"
            f"Health->{self.health} \n"
            f"Attack->{self.attack} \n"
            f"Items->{self.items}"
        )
