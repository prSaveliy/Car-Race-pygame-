class Settings():

    def __init__(self):
        self.screen_width = 512
        self.screen_height = 970
        self.bg_color = (210, 210, 210)

        self.lines_color = (110, 110, 110)
        self.lane_width = self.screen_width // 3
        self.line_width = 10
        self.dash_height = 110
        self.dash_gap = 40
        self.line_offset = 0

        self.cars_left = 3
        self.cars_limit = 2

        self.speed_increase_scale = 1.03

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.barrier_speed = 0.3
        self.line_speed = 0.3
        self.star_speed = 0.3
        self.start_line_speed = 0.3
        self.message_start_speed = 0.3
        self.star_points = 10
        self.preview_color = (250, 0, 0)





