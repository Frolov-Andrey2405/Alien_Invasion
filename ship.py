import pygame


class Ship():
    """Класс для отображения корабля"""

    def __init__(self, ai_game):

        # Инициализирует корабль и задает его начальную позицию
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаті центра корабля
        self.x = float(self.rect.x)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        # Обновляется атрибутом x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.speed_ship
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.speed_ship

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
