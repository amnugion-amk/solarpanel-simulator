import pygame
import resources

def ccW(startPos, endPos, targetPos):
    return (endPos[0] - startPos[0]) * (targetPos[1] - startPos[1]) > (endPos[1] - startPos[1]) * (targetPos[0] - startPos[0])

def checkIntersect(a, b, c, d):
    return (ccW(a, c, d) != ccW(b, c, d)) and (ccW(a, b, c) != ccW(a, b, d))  

class sunClass():
    def __init__(self, screenWidth, screenHeight):
        self.width = screenWidth
        self.height = screenHeight
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/sun.png").convert_alpha(),
            (150, 150)
        )
        self.rect = self.image.get_rect()
        self.startX = screenWidth
        self.endX = -65
        
        self.startY = screenHeight
        self.endY = screenHeight
        
        self.yPeak = screenHeight
        
        self.progress = 0
        self.speed = 0.005
        
        self.energyAbsorbed = 0
        self.energyBlocked = 0
        self.energyTotal = 0
        
    def update(self, surface):
        if self.progress <= 1:
            currX = self.startX + (self.endX-self.startX) * self.progress
            currY = self.startY + (self.endY-self.startY) * self.progress
            
            currY += -4 * self.yPeak * self.progress * (1 - self.progress)
            
            self.rect.x = currX
            self.rect.y = currY
            
            self.progress += self.speed
            if len(resources.panels) < 1: return
            pointA = self.rect.center
            pointB = resources.panels[0].centerPos
            
            pathBlocked = False
            
            if len(resources.objects) >= 1:
                for barrier in resources.objects:
                    if (checkIntersect(pointA, pointB, barrier.startPos, barrier.endPos)):
                        pathBlocked = True
                        break
            
            color = None
            if pathBlocked:
                self.energyBlocked += 1
                color = (255, 0, 0) 
            else:
                self.energyAbsorbed += 1
                color = (0, 255, 0)
            self.energyTotal = self.energyAbsorbed + self.energyBlocked
            
            pygame.draw.line(surface, color, pointA, pointB, 3)
                
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.progress = 0
        self.energyAbsorbed = 0
        self.energyBlocked = 0
        self.energyTotal = 0
        
    def requestResults(self):
        if self.energyAbsorbed == 0 or self.energyTotal == 0:
            return 0
        return (self.energyAbsorbed/self.energyTotal)*100