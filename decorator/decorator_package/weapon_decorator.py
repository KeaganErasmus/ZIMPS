from .player_decorator import PlayerDecorator


class WeaponDecorator(PlayerDecorator):
    def __init__(self, player, weapon_name, weapon_attack):
        super().__init__(player)
        self.weapon_name = weapon_name
        self.weapon_attack = weapon_attack

    def get_details(self):
        details = super().get_details()
        return (f"{details} \n"
                "Weapon->" + self.weapon_name +
                f" (Attack+{self.weapon_attack})")

    def get_attack(self):
        # Enhance attack value
        return self.player.get_attack() + self.weapon_attack
