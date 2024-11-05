class ActionStrategy:
    def execute(self, game, *args):
        raise NotImplementedError(
            "This method should be overridden by subclasses")
