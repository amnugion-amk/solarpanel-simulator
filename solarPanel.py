import pygame
import renderService
import physicsObjects

placingPanel = False
physicsObjectStorage = renderService.physicsObjectsStorage

def checkSolarPanel():
    return len(physicsObjectStorage.solarPanel) == 1

def initPlacement():
    if checkSolarPanel(): return
    
    global currentPanel, placingPanel
    startPos = pygame.mouse.get_pos()
    
    physicsObjectStorage.solarPanel.append(physicsObjects.line(startPos, startPos, (0, 0, 255), 10))
    
    placingPanel = True
    
def whilePlacement():
    global placingPanel
    if not placingPanel: return
    physicsObjectStorage.solarPanel[-1].endPos = pygame.mouse.get_pos()
    
def finalizePlacement():
    global placingPanel
    if not placingPanel: return
    
    placingPanel = False
    
def remove():
    global placingPanel
    if not checkSolarPanel(): return
    
    placingPanel = False
    del physicsObjectStorage.solarPanel[-1]