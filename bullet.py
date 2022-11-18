import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблём"""

    def __init__(self, ai_game):
        # Созда'т обїект снарядов в текущей позиции корабля
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # Создание снаряда в позиции (0, 0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0,
            self.setting.bullet_width,
            self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция снаряда хранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        
        # Обновление позиции снаряда в вещественном формате
        self.y -= self.setting.bullet_speed

        #Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        #Вывод снаряда на экран
        pygame.draw.rect(self.screen, self.color, 
            self.rect)
