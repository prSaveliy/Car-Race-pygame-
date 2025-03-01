class GameStats():

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self._reset_stats()

        self.game_active = False
        self.countdown_active = False
        self.score = 0
        self.record = 0

    def _reset_stats(self):
        self.settings.cars_left = self.settings.cars_limit
