from pygame.sprite import Sprite
import pygame

from car import Car

class LivesBoard(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game

        self.cars = pygame.sprite.Group()
        self.prep_cars()

    def prep_cars(self):
        self.cars.empty()
        for car_number in range(self.settings.cars_left + 1):
            car = Car(self.ai_game, 40,40)
            car.rect.x = 10 + car.rect.width * car_number
            car.rect.y = 20
            self.cars.add(car)

    def draw_cars(self):
        self.cars.draw(self.screen)