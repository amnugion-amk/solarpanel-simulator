import pygame
import settings
import UImanager

screenDimensions = settings.size

class basicUI:
    def __init__(self, pos, size, color, radius=2):
        self.currentSize = size
        self.currentPos = pos
        
        self.currentColor = color
        self.radius = radius
        
        self.rect = None
        self.updateRect(pos, size)
        
        self.enabled = True

    def updateRect(self, pos, size):
        self.rect = pygame.Rect(
            pos[0],
            pos[1],
            size[0],
            size[1]
        )
        
    def draw(self, screen):
        if not self.enabled: return
        self.updateRect(self.currentPos, self.currentSize)
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)

class imageUI(basicUI):
    def __init__(self, pos, size, color, image, imageSize, radius=2):
        super().__init__(pos, size, color, radius)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), imageSize)
        self.updateRect(
            pos,
            (self.image.get_width(), self.image.get_height())
        )
    def draw(self, screen):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        screen.blit(self.image, self.rect)

controlsUISize = (320, 250)
controlsUIPos = (screenDimensions[0]/2-controlsUISize[0]/2,screenDimensions[1]/2-controlsUISize[1]/2) 

controlsUIObj = imageUI(controlsUIPos, controlsUISize, (255, 255, 255), "sprites/controls.png", controlsUISize)
controlsUIObj.enabled = False