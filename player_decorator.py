from player import Player


class PlayerDecorator(Player):
    def __init__(self, player: Player):
        self._player = player

    def get_location(self):
        return self._player.get_location()

    def get_attack(self):
        return self._player.get_attack()

    def get_items(self):
        return self._player.get_items()

    def get_health(self):
        return self._player.get_health()

    def take_damage(self, amount):
        self._player.take_damage(amount)

class HealthBuffDecorator(PlayerDecorator):
    def __init__(self, player: Player, bonus_health: int):
        super().__init__(player)
        self.bonus_health = bonus_health

    def get_health(self):
        return self._player.get_health() + self.bonus_health

class AttackBuffDecorator(PlayerDecorator):
    def __init__(self, player: Player, bonus_attack: int):
        super().__init__(player)
        self.bonus_attack = bonus_attack

    def get_attack(self):
        return self._player.get_attack() + self.bonus_attack
