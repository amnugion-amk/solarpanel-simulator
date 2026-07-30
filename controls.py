import pygame
import settings

class controlsUI:
    def __init__(self):
        self.image = pygame.transform.scale((pygame.image.load("sprites/controls.png").convert_alpha()), (320, 250))
        self.rect = self.image.get_rect()
        self.rect.x = 0 
        self.rect.y = settings.size[1]-self.image.get_height() - 15
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)