import pygame

class StartLine():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.width = 512
        self.height = 10
        self.color = (70, 70, 70)

        self.rect = pygame.Rect(0, 850, self.width, self.height)

        self.y = float(self.rect.y)

    def update_start_line(self):
        self.y += self.settings.start_line_speed
        self.rect.y = self.y

    def reset_position(self):
        self.rect.x = 0
        self.rect.y = 850

    def draw_start_line(self):
        pygame.draw.rect(self.screen, self.color, self.rect)