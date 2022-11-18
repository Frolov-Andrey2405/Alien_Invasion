import pygame


class Ship():
    """Class for ship display"""

    def __init__(self, ai_game):

        # Initializes the ship and sets its initial position
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image of the ship and gets a rectangle
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom edge of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving the real coordinate of the ship's center
        self.x = float(self.rect.x)

        # Flags of displacement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates ship's position based on the flag"""
        # Updated with x attribute, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.speed_ship
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.speed_ship

        # Update the rect attribute based on self.x
        self.rect.x = self.x

    def blitme(self):
        # Draws the ship at the current position
        self.screen.blit(self.image, self.rect)
