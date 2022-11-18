import sys
import pygame

# ---------------------------
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
# ---------------------------


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Иницциализирует игру и создаёт игровые ресурсы"""
        pygame.init()

        # ---------------------------
        self.setting = Setting()
        # ---------------------------

        # Создание окна
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
        """Запуск основного цикла игры"""
        key = True
        while (key):
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self._create_fleet()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            # Завершение работы
            if event.type == pygame.QUIT:
                sys.exit()

            # Класс для управление кораблём
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        # Завершение работы по нажатию клавиши Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Создание флота вторжения"""

        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране"""
        ship_height = self.ship.rect.height
        available_space_y = (
            self.setting.screen_height -
            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание флота вторжения
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = ( alien.rect.height + 2 *
                    alien.rect.height * row_number )
        self.aliens.add(alien)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""

        # Обновление позиции снарядов
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.setting.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск кода
    ai = AlienInvasion()
    ai.run_game()
