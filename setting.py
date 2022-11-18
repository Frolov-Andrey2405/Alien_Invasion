class Setting():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        '''Инициализирует настройки игры'''

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.background_color = (230, 230, 230)

        # Настройки корабля
        self.speed_ship = 10

        # Параметры снаряда
        self.bullet_speed = 25
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
