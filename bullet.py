import pygame

# --------------------------------
from pygame.sprite import Sprite
# --------------------------------


class Bullet(Sprite):
    '''A class that manages projectiles fired by the spaceship'''

    def __init__(self, ai_settings, screen, ship):
        '''Creates an object for the projectile at the spacecraft's current position.'''
        super().__init__()
        self.screen = screen

        # Create a rectangle for the projectile at (0, 0) and then set the correct position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store projectile position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''Move the projectile to the top of the screen.'''
        # Update the decimal position of the projectile
        self.y -= self.speed_factor
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the projectile on the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
