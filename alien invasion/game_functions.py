import sys
import pygame

def check_events(ship):                             # Реакции на нажатие клавиш
      for event in pygame.event.get():  
            if event.type == pygame.QUIT:         
                sys.exit() 
            elif event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                       ship.moving_right = False 

def update_screen(ai_settings, screen, ship):          # Обновление экрана при нажатии клавиш, то есть отображение перемешения корабля 
    screen.fill(ai_settings.bg_color)
    ship.blitme

    pygame.display.flip()

