import pygame
from pygame.sprite import Sprite

class Car(Sprite):

    def __init__(self, ai_game, width, height):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.current_lane = 1
        self.lane_positions = [
            self.settings.lane_width // 2,
            self.settings.screen_width // 2,
            self.settings.screen_width - self.settings.lane_width // 2
        ]

        self.rect.centerx = self.lane_positions[self.current_lane]
        self.rect.bottom = self.screen_rect.bottom - 10

        self.move_right = False
        self.move_left = False

    def update(self, direction):
        if direction == "left" and self.current_lane > 0:
            self.current_lane -= 1
        elif direction == "right" and self.current_lane < 2:
            self.current_lane += 1

        self.rect.centerx = self.lane_positions[self.current_lane]

    def blit_car(self):
        self.screen.blit(self.image, self.rect)

    def center_car(self):
        self.current_lane = 1
        self.rect.centerx = self.lane_positions[self.current_lane]
        self.rect.bottom = self.screen_rect.bottom - 10




