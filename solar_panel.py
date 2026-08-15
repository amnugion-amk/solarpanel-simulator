import pygame
import resources

placingPanel = False
startPos = ((0, 0))
currentPanel = None

class solarPanel():
    def __init__(self, startPos, endPos, color=(255, 255, 255), width=10):
        self.startPos = startPos
        self.endPos = endPos
        self.color = color
        self.width = width
    
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.startPos, self.endPos, self.width)
    
def initiatePanelPlacement():
    global placingPanel, startPos, currentPanel
    placingPanel = True
    startPos = pygame.mouse.get_pos()
    currentPanel = solarPanel(startPos=startPos, endPos=startPos, color=(3, 44, 255), width=10)
    
def finalizePanelPlacement():
    global placingPanel
    placingPanel = False
    resources.panels.append(currentPanel)
    
    currentPanel.centerPos = (
        currentPanel.startPos[0] + (currentPanel.endPos[0]-currentPanel.startPos[0]) * 0.5,
        currentPanel.startPos[1] + (currentPanel.endPos[1]-currentPanel.startPos[1]) * 0.5
    )
    
def whilePanelPlacement(screen):
    currentPanel.endPos = pygame.mouse.get_pos()
    currentPanel.draw(screen)
    
def removePanel():
    global placingPanel, startPos, currentPanel
    if (len(resources.panels) == 0): return
    
    del resources.panels[0]
    
    placingPanel = False
    startPos = ((0, 0))
    currentPanel = None