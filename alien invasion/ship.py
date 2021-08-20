class Ship():   
    def __init__(self, screen):                             # Метод init получает аргумент screen на котором выводится корабль and self 
        self.image = pygame.image.load()                    # Здесь проводитс загрузка изображения
        self.rect = self.image.get_rect()                   # Метод get_rect используется
        self.screen_rect = screen.get_rect()                # 1
        self.screen_rect = screen.get_rect()                #
        self.rect.centerx = self.screen_rect.centerx        #
        self.rect.bottom = self.screen_rect.bottom          #
    def blitme(self):                                       #
        self.screen.blit(self.image, self.rect)             #
