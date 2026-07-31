import pygame
import controls
import settings
import UImanager

screenDinmensions = settings.size

font = pygame.font.Font(None, 24)

class text():
    def __init__(self, fontSize, color, text, anchorPoint):
        self.font = pygame.font.Font(None, fontSize)
        self.currentColor = color
        self.currentText = text
        
        self.textSurface = font.render(self.currentText, True, self.currentColor)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = anchorPoint
        
    def draw(self, screen):
        self.textSurface = font.render(self.currentText, True, self.currentColor)
        screen.blit(self.textSurface, self.textRect)

class button():
    def __init__(self, textString, pos, size, onPressed, colorOnHover, colorNormal):
        self.colorOnHover = colorOnHover
        self.colorNormal = colorNormal
        
        self.pos = pos
        self.size = size
        
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.onPressed = onPressed
        
        self.currentColor = self.colorNormal
        
        self.textString = textString
        self.textLabel = text(24, (0, 0, 0,), self.textString, self.rect.center)
        
        self.isMouseHovering = False
        
        
        
    def draw(self, screen, isColliding):
        self.currentColor = self.colorOnHover if isColliding else self.colorNormal
        
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=2)
        self.textLabel.draw(screen)
    def update(self, events, screen):
        mousePos = pygame.mouse.get_pos()
        isColliding = self.rect.collidepoint(mousePos)
        
        self.draw(screen, isColliding)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isColliding:
                self.onPressed()
        
def onPressedControlsButton():
    print("pressed!")
    controls.controlsUIObj.enabled = not controls.controlsUIObj.enabled
    
def onPressedSimulateButton():
    print("pressed!")
   
size = (80, 23)
posOffsets = (5, -10)
    
controlsButton = button(
    "Controls",
    (0+posOffsets[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    size,
    onPressedControlsButton,
    (225, 225, 225),
    (255, 255, 255)    
)

simulationButton = button(
    "Delete All",
    (0+posOffsets[0]*2+size[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    size,
    onPressedSimulateButton,
    (225, 225, 225),
    (255, 255, 255) 
)

helpButton = button(
    "?",
    (0+posOffsets[0]*3+size[0]*2, screenDinmensions[1]-size[1]+posOffsets[1]),
    (25, 23),
    onPressedSimulateButton,
    (225, 225, 225),
    (255, 255, 255) 
)

beginButton = button(
    "Begin",
    (screenDinmensions[0]-size[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    (75, 23),
    onPressedSimulateButton,
    (225, 225, 225),
    (255, 255, 255) 
)