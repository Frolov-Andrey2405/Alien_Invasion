import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing one alien"""

    def __init__(self, ai_game):
        """Initializes the alien and sets its initial position."""
        super().__init__()
        self.screen = ai_game.screen

        # Loading the squiggle image and assigning the attribute rect
        self.image = pygame.image.load('Alien_Invasion\images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen
        self.rect.y = self.rect.width
        self.rect.x = self.rect.height

        # Maintaining the exact horizontal position of the alien
        self.x = float(self.rect.x)
