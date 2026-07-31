import pygame
import settings

screenDimensions = settings.size

class background():
    def __init__(self):
        self.width = screenDimensions[0]
        self.height = screenDimensions[1]
        
        self.image = pygame.transform.smoothscale(pygame.image.load("sprites/background.png").convert_alpha(), screenDimensions)
        self.rect = self.image.get_rect()
        self.rect.x = (self.width/2)-self.width/2
        self.rect.y = (self.height/2)-self.height/2
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        