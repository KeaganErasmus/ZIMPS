from action_strategy import ActionStrategy


class BashStrategy(ActionStrategy):
    def execute(self, game, direction):
        game.bash_through_wall(direction)