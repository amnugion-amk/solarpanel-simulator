import pygame
import resources
import settings
import result
import math
import button

originalBackground = settings.originalColors
showingSun = False

def ccW(startPos, endPos, targetPos):
    return (endPos[0] - startPos[0]) * (targetPos[1] - startPos[1]) > (endPos[1] - startPos[1]) * (targetPos[0] - startPos[0])

def checkIntersect(a, b, c, d):
    return (ccW(a, c, d) != ccW(b, c, d)) and (ccW(a, b, c) != ccW(a, b, d))  


class sunClass():
    def __init__(self, screenWidth, screenHeight):
        global showingSun
        self.width = screenWidth
        self.height = screenHeight
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/sun.png").convert_alpha(),
            (200, 200)
        )
        self.rect = self.image.get_rect()
        self.startX = screenWidth
        self.endX = -65
        
        self.startY = screenHeight
        
        self.yPeak = screenHeight + self.rect.height
        
        self.progress = 0
        self.speed = 0.0025
        
        self.energyAbsorbed = 0
                
        self.energyTotal = 0
        
    def update(self, surface):
        if self.progress <= 1:
            currX = self.startX + (self.endX-self.startX) * self.progress            
            currY = self.startY - math.sin(self.progress*math.radians(180))*self.yPeak
            
            self.rect.x = currX
            self.rect.y = currY
            
            self.progress += self.speed
            
            if len(resources.panels) < 1: return
            pointA = self.rect.center
            pointB = resources.panels[0].centerPos
            
            lineColor = (0, 255, 0) 
            pathBlocked = False
            energyBlockedModifier = 0
            
            for sunlightBlocked, blockerTree in resources.blockers.items():
                if blockerTree == resources.clouds and not button.toggleClouds.ticked: continue
                for blocker in blockerTree:
                    if (checkIntersect(pointA, pointB, blocker.startPos, blocker.endPos)):
                        pathBlocked = True
                        energyBlockedModifier = sunlightBlocked 
                        lineColor = (255, 0, 0) 
                        
                        break
            self.energyTotal += 1        
            self.energyAbsorbed += 1-energyBlockedModifier
            pygame.draw.line(surface, lineColor, pointA, pointB, 3)
        elif self.progress >= 1:
            showingSun = False
            result.resultBarObj.textLabel.currentText = result.formatEfficiency(self.requestResults())
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.progress = 0
        self.energyAbsorbed = 0
        self.energyBlocked = 0
        self.energyTotal = 0
        settings.background = settings.originalColors
        
    def requestResults(self):
        if self.energyTotal == 0:
            return 0
        return (self.energyAbsorbed/self.energyTotal)*100

sunObj = sunClass(settings.size[0], settings.size[1])
