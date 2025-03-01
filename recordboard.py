import pygame.font

class RecordBoard():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.color = (70, 70, 70)
        self.font = pygame.font.SysFont(None, 48)

    def prep_record(self, msg):
        rounded_record = round(self.stats.record)
        record_str = "{:,}".format(rounded_record)
        record_message = f"{msg}: {record_str}"
        self.record_image = self.font.render(record_message, True,
                                 self.color, self.settings.bg_color)

        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.top = 15

    def draw_record(self):
        self.screen.blit(self.record_image, self.record_rect)

    def check_record(self):
        if self.stats.score > self.stats.record:
            self.stats.record = self.stats.score
            self.prep_record("High Score")

