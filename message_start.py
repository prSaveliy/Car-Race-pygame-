import pygame.font

class MessageStart():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.color = (70, 70, 70)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_start_message("Start")

    def prep_start_message(self, msg):
        self.image = self.font.render(msg, True,
                                      self.color, self.settings.bg_color)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 800
        self.y = float(self.rect.y)

    def update_start_message(self):
        self.y += self.settings.message_start_speed
        self.rect.y = self.y

    def draw_start_message(self):
        self.screen.blit(self.image, self.rect)


