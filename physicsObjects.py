import pygame
import renderService
import settings
import customMath
import result

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
        self.centerPos = customMath.lerp(currStart, currEnd, 0.5)
        self.prevPositions = currPos
        
    def render(self, screen):
        self.checkForChanges()
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
        self.speed = 0.003
        
        self.rect.x = self.startX
        self.rect.y = self.yBase
        
        self.showingSun = False
        
        self.blocked = 0
        self.total = 0
        
        self.resetPos()
         
    def render(self, screen):
        if not self.showingSun: return
        
        if self.progress < 1:
            self.rect.x = self.startX + (self.endX-self.startX) * self.progress
            self.rect.y = customMath.sineHalfCircle(self.yPeak, self.yBase, self.progress)
            self.progress += self.speed
            
            if len(physicsObjectStorage.solarPanel) != 1: self.draw(screen); return
            solarPanel = physicsObjectStorage.solarPanel[0]
            rayColor = (0, 255, 0)
            
            sunCenter = self.rect.center
            solarPanelCenter = solarPanel.centerPos
            
            for barrier in physicsObjectStorage.barriers:
                if customMath.checkIntersect(sunCenter, solarPanelCenter, barrier.startPos, barrier.endPos):
                    rayColor = (255, 0, 0)
                    self.blocked += 1
                    break
                
            self.total += 1
            
            pygame.draw.line(screen, rayColor, sunCenter, solarPanelCenter, 5)
            self.draw(screen)
        else:
            self.endCycle()
            
    def endCycle(self):
        self.progress = 0
        self.showingSun = False
        
        result.resultBarObj.textLabel.currentText = result.formatResults(self.requestResults())
        
        self.total = 0
        self.blocked = 0
        
        self.resetPos()
        
    def resetPos(self):
        self.rect.x = self.startX
        self.rect.y = self.yBase
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def requestResults(self):
        absorbed = self.total-self.blocked
        return absorbed/self.total*100 if self.total != 0 else 0
    
physicsObjectStorage.sun.append(sun())