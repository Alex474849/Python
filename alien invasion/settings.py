
# Этот класс поможет нам выводить все настройки в игре, чтобы не лезть в код постоянно
class Settings():
    def __init__(self):
        self.screen_width = 1700
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1 
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 10, 30, 100 
