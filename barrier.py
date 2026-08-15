import pygame

import renderService
import physicsObjects

placingBarrier = False
currentBarrier = None

physicsObjectStorage = renderService.physicsObjectsStorage

def initPlacement():
    global placingBarrier, currentBarrier
    if placingBarrier: return
    
    placingBarrier = True
    
    mousePos = pygame.mouse.get_pos()
    currentBarrier = physicsObjects.line(mousePos, mousePos, (0, 0, 0), 14)
    renderService.physicsObjectsStorage.barriers.append(currentBarrier)
    
def whilePlacement():
    global currentBarrier
    if not currentBarrier or not placingBarrier: return
    
    currentBarrier.endPos = pygame.mouse.get_pos()
    
def finalizePlacement():
    global currentBarrier, placingBarrier
    placingBarrier = False
    currentBarrier = None
    
def removeLatestBarrier():
    global placingBarrier
    if len(physicsObjectStorage.barriers) == 0 or placingBarrier: return
    
    del physicsObjectStorage.barriers[-1]