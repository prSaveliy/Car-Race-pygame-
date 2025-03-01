import sys

import pygame

from random import randint

from time import sleep

from settings import Settings
from button import Button
from start_line import StartLine
from recordboard import RecordBoard
from scoreboard import ScoreBoard
from lives_board import LivesBoard
from message_start import MessageStart
from go_123 import Go123
from game_stats import GameStats
from car import Car
from barrier import Barrier
from star import Star

class CarRace:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Car Race")

        self.play_button = Button(self, "Play")

        self.start_line = StartLine(self)

        self.stats = GameStats(self)

        self.record = RecordBoard(self)

        self.start_message = MessageStart(self)

        self.go123 = Go123(self)

        self.lives = LivesBoard(self)

        self.score = ScoreBoard(self)

        self.car = Car(self, 70,70)

        self.barriers = pygame.sprite.Group()
        self.last_barrier_time = pygame.time.get_ticks()

        self.stars = pygame.sprite.Group()
        self.last_star_time = pygame.time.get_ticks()

        self.last_increase_time = pygame.time.get_ticks()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.countdown_active:
                self._handle_countdown()
            elif self.stats.game_active:
                self.start_message.update_start_message()
                self.barriers.update()
                self.stars.update()
                self._update_barriers()
                self._update_stars()
                self._increase_speed()
                self._create_barriers()
                self._create_stars()
                self._update_offset()

            self._update_screen()

    def _update_offset(self):
        self.settings.line_offset += self.settings.line_speed
        if self.settings.line_offset >= self.settings.dash_height + self.settings.dash_gap:
            self.settings.line_offset = 0

    def _draw_lines(self):
        for i in range(1, 3):
            x = i * self.settings.lane_width
            for y in range(-self.settings.dash_height, self.settings.screen_height,
                           self.settings.dash_height + self.settings.dash_gap):
                line_top = y + self.settings.line_offset
                line_bottom = line_top + self.settings.dash_height

                start_line_bottom = self.start_line.rect.bottom
                if line_bottom > start_line_bottom:
                    continue

                pygame.draw.rect(
                    self.screen,
                    self.settings.lines_color,
                    (x - self.settings.line_width // 2, line_top,
                     self.settings.line_width, self.settings.dash_height)
                )

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active and not self.stats.countdown_active:
            self.stats.countdown_active = True
            self.current_321_time = pygame.time.get_ticks()
            self.countdown_value = 3
            pygame.mouse.set_visible(False)

    def _handle_countdown(self):
        current_time = pygame.time.get_ticks()
        try:
            if current_time - self.current_321_time >= 1000:
                self.countdown_value -= 1
                self.current_321_time = current_time
                if self.countdown_value == 0:
                    self.countdown_value = "Go!"
        except TypeError:
            self.stats.countdown_active = False
            self._reset_game()
            self.stats.game_active = True

    def _reset_game(self):
        self.stats._reset_stats()
        self.settings.initialize_dynamic_settings()

        self.start_line = StartLine(self)

        self.stats.score = 0
        self.score.prep_score()
        self.lives.prep_cars()
        self.barriers.empty()
        self._create_barriers()
        self._create_stars()
        self.car.center_car()
        self.start_message.prep_start_message("Start")

    def _check_start_line_game_active(self):
        if self.stats.game_active == False:
            self.start_line.draw_start_line()
            self.start_line.reset_position()
        if self.stats.game_active == True:
            self.start_line.draw_start_line()
            self.start_line.reset_position()
            self.start_line.update_start_line()

    def _check_key_down_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.car.update("right")
        if event.key == pygame.K_LEFT:
            self.car.update("left")

    def _update_barriers(self):
        for barrier in self.barriers.copy():
            if barrier.rect.top >= self.settings.screen_height:
                self.barriers.remove(barrier)

        self._check_cars_barriers_collisions()

    def _update_stars(self):
        for star in self.stars.copy():
            if star.rect.top >= self.settings.screen_height:
                self.stars.remove(star)

        self._check_cars_stars_collisions()

    def _check_cars_barriers_collisions(self):
        if pygame.sprite.spritecollideany(self.car, self.barriers):
            self._car_hit()

    def _check_cars_stars_collisions(self):
        collided_star = pygame.sprite.spritecollideany(self.car, self.stars)
        if collided_star:
            self.stars.remove(collided_star)
            self.stats.score += self.settings.star_points
            self.score.prep_score()

    def _create_barriers(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_barrier_time > 1000:
            num_barriers = randint(1, 2)

            lanes = [0, 1, 2]
            for _ in range(num_barriers):
                if lanes:
                    random_lane = lanes.pop(randint(0, len(lanes) - 1))
                    barrier = Barrier(self)
                    barrier.rect.x = (random_lane * self.settings.lane_width +
                                      self.settings.lane_width // 2 - barrier.rect.width // 2)
                    barrier.rect.y = -barrier.rect.height
                    self.barriers.add(barrier)

            self.last_barrier_time = current_time

    def _create_stars(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_star_time > 3500:
            num_stars = randint(1, 2)

            lanes = [0, 1, 2]
            for _ in range(num_stars):
                if lanes:
                    random_lane = lanes.pop(randint(0, len(lanes) - 1))
                    star = Star(self)
                    star.rect.x = (random_lane * self.settings.lane_width +
                                        self.settings.lane_width // 2 - star.rect.width // 2)
                    star.rect.y = -star.rect.height

                    if not any(barrier.rect.colliderect(star.rect) for barrier in self.barriers):
                        self.stars.add(star)

            self.last_star_time = current_time

    def _car_hit(self):
        if self.settings.cars_left > 0:
            self.settings.cars_left -=1
            self.lives.prep_cars()

            self.barriers.empty()
            self._create_barriers()

            self.stars.empty()
            self._create_stars()

            self.car.center_car()

            sleep(1.5)
        else:
            self.stats.game_active = False
            self.barriers.empty()
            self.stars.empty()
            self.start_message.prep_start_message("Start")
            pygame.mouse.set_visible(True)

    def _increase_speed(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_increase_time > 5000:
            self.settings.barrier_speed *= self.settings.speed_increase_scale
            self.settings.line_speed *= self.settings.speed_increase_scale
            self.settings.star_speed *= self.settings.speed_increase_scale

            self.last_increase_time = current_time

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        if self.stats.countdown_active:
            self.go123.prep_go123(str(self.countdown_value))
            self.go123.draw_go123()
            self._check_start_line_game_active()
            self.start_message.draw_start_message()
            self._draw_lines()
            self.car.blit_car()
            self.barriers.draw(self.screen)
            self.stars.draw(self.screen)
            self.car.center_car()
        elif not self.stats.game_active:
            self.play_button.draw_button()
            self.record.check_record()
            self.record.prep_record("High Score")
            self.record.draw_record()
        else:
            self._check_start_line_game_active()
            self.start_message.draw_start_message()
            self._draw_lines()
            self.car.blit_car()
            self.barriers.draw(self.screen)
            self.stars.draw(self.screen)
            self.score.draw_score()
            self.lives.draw_cars()

        pygame.display.flip()

if __name__ == '__main__':
    cr = CarRace()
    cr.run_game()