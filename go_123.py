import pygame.font

class Go123():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.color = self.settings.preview_color
        self.font = pygame.font.SysFont(None, 48)

    def prep_go123(self, msg):
        self.image = self.font.render(msg, True,
                                      self.color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def draw_go123(self):
        self.screen.blit(self.image, self.image_rect)