import sys
import pygame

# ---------------------------
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
# ---------------------------


class AlienInvasion():
    """Class for managing resources and game behavior"""

    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()

        # ---------------------------
        self.setting = Setting()
        # ---------------------------

        # Creating a window
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # ---------------------------
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # ---------------------------

    def run_game(self):
        """Starting the main game cycle"""
        key = True
        while (key):
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self._create_fleet()

    def _check_events(self):
        """Handles keystrokes and mouse events"""
        for event in pygame.event.get():
            # Finishing the job
            if event.type == pygame.QUIT:
                sys.exit()

            # Class for controlling the ship
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reacts to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Quit by pressing Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to Key Release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating a new projectile and adding it to the bullets group"""
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Creating the Invasion Fleet"""

        # Creating an alien and calculating the number of aliens in a row
        # The interval between neighboring aliens is the width of the alien

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Specifies the number of rows that fit on the screen."""
        ship_height = self.ship.rect.height
        available_space_y = (
            self.setting.screen_height -
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Creating an invasion fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Creating an alien and placing it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _update_bullets(self):
        """Updates projectile positions and destroys old projectiles"""

        # Updating projectile positions
        self.bullets.update()

        # Removing projectiles that are over the edge of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """Updates the screen image and displays a new screen"""
        self.screen.fill(self.setting.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Display the last screen drawn
        pygame.display.flip()


if __name__ == "__main__":
    # Create an instance and run the code
    ai = AlienInvasion()
    ai.run_game()
