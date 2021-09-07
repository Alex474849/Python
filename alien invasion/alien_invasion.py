
import sys                      # Модуль sys  будет завершать по команде игру
import pygame
from pygame.sprite import Group                   # Модуль pygame содержит всю функциаеалность для создания игры
from settings import Settings   # иморптруем settings
from ship1 import Ship          # импортируем ship
import game_functions as gf

def run_game():                 #   Определяем функцию
    pygame.init()               #   Инициализруем настроки pygame
    ai_settings = Settings()      # Ипортируем класс settigs и вставляем ai_settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Используем атрибуты для создания формата окна 

    screen = pygame.display.set_mode((1700, 1000))    #    Создаем отображаемую область, аргуметы означают размеры игрового окна
    pygame.display.set_caption("Alien Invasion")       #    Отображение названия игры     
    bg_color = (230, 230, 230)                          # выбрали цвет экрана
    ship = Ship(ai_settings, screen)
    bullets = Group()                            # Создаем корабль до начала цикла while

    while True:                                     # Запускаем цикл
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)                                     
        for event in pygame.event.get():            # Чтобы наша прогрмма реагировала на акие либо действия напишем цикл for. Используем метод pygame.event.get():, чтобы получать доступ к событиям
            if event.type == pygame.QUIT:           # Пишем if для обнаружение и обработки конкретных действий
                sys.exit()                          # Например мы закрываем программа, он обнаруживает  pygame.QUIT: и вызывает sys.exit() который завершает игру
            screen.fill(bg_color)                   # Заполняем экран выбранным цветом фона
            screen.fill(ai_settings.bg_color)       # Используем атрибут для создания цвкта фона
            ship.blitme()                           # Выводим корабль поверх фона
            

        pygame.display.flip()                       #   При запуске буде твыводиться новый экран
        
run_game()  #   Запускаем игру