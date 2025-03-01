import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/star.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.y = -self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.star_speed
        self.rect.y = self.y