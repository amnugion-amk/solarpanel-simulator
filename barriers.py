import pygame
import resources

placingBarrier = False
startPos = ((0, 0))
currentBarrier = None

class barrier():
    def __init__(self, startPos, endPos, color=(15, 15, 15), width=20):
        self.startPos = startPos
        self.endPos = endPos
        self.color = color
        self.width = width
        pass
    
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.startPos, self.endPos, self.width)

def initiateBarrierPlacement():
    global placingBarrier, startPos, currentBarrier
    placingBarrier = True
    startPos = pygame.mouse.get_pos()
    currentBarrier = barrier(startPos=startPos, endPos=startPos, color=(15, 15, 15), width=15)
    
def finalizeBarrierPlacement():
    global placingBarrier, currentBarrier
    placingBarrier = False
    resources.objects.append(currentBarrier)
    currentBarrier = None
    
def whileBarrierPlacement(screen):
    currentBarrier.endPos = pygame.mouse.get_pos()
    currentBarrier.draw(screen)
    
def removeBarrier():
    global placingBarrier, startPos, currentBarrier
    
    placingBarrier = False
    startPos = ((0, 0))
    currentBarrier = None