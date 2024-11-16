from .player_decorator import PlayerDecorator


class ArmorDecorator(PlayerDecorator):
    def __init__(self, player, armor_points):
        super().__init__(player)
        self.armor_points = armor_points

    def get_details(self):
        details = super().get_details()
        return f"{details} \nArmor->{self.armor_points}"

    def get_health(self):
        # Modify health behavior with armor
        return self.player.get_health() + self.armor_points
