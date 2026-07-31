import pygame
import settings
import UImanager

screenDimensions = settings.size

class controlsUI:
    def __init__(self):
        self.image = pygame.transform.scale((pygame.image.load("sprites/controls.png").convert_alpha()), (320, 250))
        self.imageRect = self.image.get_rect()
        width = self.image.get_width()
        height = self.image.get_height()
        
        self.rect = pygame.Rect(
            screenDimensions[0]/2-width/2,
            screenDimensions[1]/2-height/2,
            width,
            height
        )
        
        self.currentColor = (255, 255, 255)
        
        self.enabled = False
        
    def draw(self, screen):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=8)
        screen.blit(self.image, self.rect)
        
controlsUIObj = controlsUI()