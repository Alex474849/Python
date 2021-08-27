import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('/Users/alexey/Dropbox/Мой Mac (FeelQueen’s iMac)/Documents/Python/rocket-147466_640.bmp') # Возврашает картинку коробля
        self.rect = self.image.get_rect()       # С поиощью метода get получили изображение
        self.screen_rect = screen.get_rect()    #
        self.rect.centerx = self.screen_rect.centerx    
        self.rect.bottom = self.screen_rect.bottom      # центрируем изоюражение
        self.moving_right = False
        self.moving_left = False
    def update(self):                                   # Этот метод перемешает корабль, есди флаг self.moving_right = True
       if self.moving_right == True:
          self.rect.centerx += 1
       if self.moving_left == True:
          self.rect.centerx -= 1
    def blitme(self):
            self.screen.blit(self.image, self.rect)   

        