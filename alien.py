import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задаёт его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображениея прищельца и назначение атрибута rect
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.y = self.rect.width
        self.rect.x = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
