import pygame
import renderService
import settings
import customMath

screenSize = settings.screenSize
physicsObjectStorage = renderService.physicsObjectsStorage

class line():
    def __init__(self, startPos, endPos, color, width):
        self.startPos = startPos
        self.endPos = endPos
        self.prevPositions = (self.startPos, self.endPos)
        
        
        self.color = color
        self.width = width
        
        self.centerPos = customMath.lerp(startPos, endPos, 0.5)
        
        
    def checkForChanges(self):
        currStart = self.startPos
        currEnd = self.endPos
        
        currPos = (currStart, currEnd)
        
        if self.prevPositions == currPos: return
        self.centerPos = customMath.lerp(currStart, currEnd)
        self.prevPositions = currPos
        
    def render(self, screen):
        pygame.draw.line(screen, self.color, self.startPos, self.endPos, self.width)
        
class sun():
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/sun.png").convert_alpha(),
            (200, 200)
        )
        
        self.rect = self.image.get_rect()
        
        self.yPeak = 0
        self.yBase = screenSize[1]
        
        self.startX = screenSize[0]
        self.endX = 0
        
        self.progress = 0
        self.speed = 0.005
        
        self.rect.x = self.startX
        self.rect.y = self.yBase
        
        self.showingSun = True
         
    def render(self, screen):
        if not self.showingSun: return
        
        if self.progress < 1:
            self.rect.x = self.startX + (self.endX-self.startX) * self.progress
            self.rect.y = customMath.sineHalfCircle(self.yPeak, self.yBase, self.progress)
            self.progress += self.speed
            
            if len(physicsObjectStorage.solarPanel) != 1: return
            isIntersecting = False
            solarPanel = physicsObjectStorage.solarPanel[0]
            
            for barrier in physicsObjectStorage.barriers:
                if customMath.checkIntersect(self.rect.center, solarPanel):
                    
            
        screen.blit(self.image, self.rect)
        
renderService.physicsObjectsStorage.sun.append(sun())