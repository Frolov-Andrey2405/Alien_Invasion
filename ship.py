import pygame

# --------------------------------
from pygame.sprite import Sprite
# --------------------------------


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        '''Initialize the spacecraft and set its initial position'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the spacecraft image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new spaceship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the center of the spaceship
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Updates spacecraft position according to motion flags'''
        # Update the value of the center of the spaceship, not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update the rect object according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''Draw the spacecraft in its current position'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the spaceship on the screen.'''
        self.center = self.screen_rect.centerx
