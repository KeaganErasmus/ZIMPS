from decorator_package import PlayerComponent


class PlayerDecorator(PlayerComponent):
    def __init__(self, player):
        self.player = player

    def get_details(self):
        return self.player.get_details()
