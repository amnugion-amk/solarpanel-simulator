import pygame
import resources

def ccW(startPos, endPos, targetPos):
    return (endPos[0] - startPos[0]) * (targetPos[1] - startPos[1]) > (endPos[1] - startPos[1]) * (targetPos[0] - startPos[0])
    # penjelasan berada di study.png

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
        self.endX = 0
        
        self.startY = screenHeight/2
        self.endY = screenHeight/2
        
        self.yPeak = screenHeight/2
        
        self.progress = 0
        self.speed = 0.005
        
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
            color = (255, 0, 0) if pathBlocked else (0, 255, 0)
            
            pygame.draw.line(surface, color, pointA, pointB, 3)
                
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.progress = 0
        