import sys
import pygame
import settings
import UIclasses

pygame.init()

resultFont = pygame.font.Font(None, 40)
text_obj = resultFont.render("placeholder", True, (0, 0, 0))
text_objRect = text_obj.get_rect()
text_objRect.center = (settings.size[0]/2, settings.size[1]-text_obj.get_height())

screenDimensions = settings.size

def drawText(text, screen):
    text_obj = resultFont.render(text, True, (0, 0, 0))
    screen.blit(text_obj, text_objRect)
    
def formatEfficiency(value):
    return "Efficiency: " + str(int(value)) + "%"
    
class resultBar():
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        
        self.currentColor = color
        
        self.rect = pygame.Rect(
            pos[0],
            pos[1],
            size[0],
            size[1]
        )
    def draw(self, screen):
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=2)
        
barSize = (240, 23)
        
resultBarObj = resultBar(
    (screenDimensions[0]/2-barSize[0]/2, screenDimensions[1]-barSize[1]-10),
    barSize,
    (255, 255, 255)
)

textObj = UIclasses.text(24, (0, 0, 0), formatEfficiency(0), (
    resultBarObj.rect.x+resultBarObj.rect.width/2,
    resultBarObj.rect.y+resultBarObj.rect.height/2
    )
)