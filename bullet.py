import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for controlling projectiles fired by a ship"""

    def __init__(self, ai_game):
        # Creates a projectile object at the current ship position
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # Creating a projectile in position (0, 0) and assigning the correct position
        self.rect = pygame.Rect(0, 0,
                                self.setting.bullet_width,
                                self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # The position of the projectile is stored in a real format
        self.y = float(self.rect.y)

    def update(self):
        """Moves the projectile up the screen"""

        # Updating the projectile position in a real format
        self.y -= self.setting.bullet_speed

        # Refresh rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        # Projectile display
        pygame.draw.rect(self.screen, self.color, self.rect)
