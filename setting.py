class Setting():
    """Class for storing all Alien Invasion game settings"""

    def __init__(self):
        """Initializes game settings"""

        # Screen parameters
        self.screen_width = 1200
        self.screen_height = 700
        self.background_color = (230, 230, 230)

        # Ship settings
        self.speed_ship = 10

        # Projectile parameters
        self.bullet_speed = 25
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
