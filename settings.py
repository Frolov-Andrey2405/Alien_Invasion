class Settings():
    '''A class to store all Alien Invasion settings'''

    def __init__(self):
        '''Initializes static game settings.'''
        # Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Spaceship settings
        self.ship_limit = 3

        # Projectile settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        # The rate at which game speed increases
        self.speedup_scale = 1.1
        # The rate at which points for each alien increase
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Initializes settings that change as the game progresses.'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3
        # fleet_direction equal to 1 represents the right;
        # -1 represents left
        self.fleet_direction = 1

        # Punctuation
        self.alien_points = 1

    def increase_speed(self):
        '''Increases speed settings and points for each alien.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points += self.score_scale
