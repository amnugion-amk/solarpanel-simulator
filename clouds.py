import pygame
import settings
import resources
import random

spawnProbability = [1, 150]
speedProbability = [5, 10]
cloudOffset = 250

cloudBaseSize = (250, 100)
cloudSizeOffset = (-25, 45)
cloudTimerOffset = (1, 6)

maxClouds = 30
timerEnd = settings.fps*random.randint(cloudTimerOffset[0], cloudTimerOffset[1])
cloudSpawnTimer = timerEnd

class cloud:
    def __init__(self, startPos, speed, size):
        self.image = pygame.transform.scale((pygame.image.load("sprites/cloud.png").convert_alpha() ), size)
        self.rect = self.image.get_rect()

        self.posX = float(startPos[0])

        self.rect.x = int(self.posX)
        self.rect.y = startPos[1]
        
        self.speed = speed
        
        self.updateEdges()
        
    def lerpEdges(self, x, y): # jika x & y 0, maka akan berada di titik awalnya rect (top left)
        #                        jika x & y 1, maka akan berada di titik akhirnya rect (bottom right)
        #                        jika x & y 0.5, maka akan berada di titik tengahnya rect
        
        xOffset = self.rect.width * x
        yOffset = self.rect.height * y
        
        return (
            self.rect.x + xOffset,
            self.rect.y + yOffset
        )
        
    def updateEdges(self):
        self.startPos = self.lerpEdges(0, .75)#(0, 800)
        self.endPos = self.lerpEdges(1, .75)#(1920, 800)
        
    def draw(self, screen):
        self.posX += self.speed
        self.rect.x = int(self.posX)
        self.updateEdges()

        screen.blit(self.image, self.rect)
        
    
    def checkOutOfBounds(self):
        if self.rect.x > settings.size[0] + self.image.get_width()/2:
            return True
        return False
            
def spawnCloud():
    global cloudSpawnTimer, timerEnd
    if len(resources.clouds) >= maxClouds: return
    if cloudSpawnTimer >= timerEnd:
        resources.clouds.append(
            cloud(
                (-cloudBaseSize[0]-cloudSizeOffset[1], random.randint(0, cloudOffset)),
                random.randint(speedProbability[0], speedProbability[1])/10,
                (
                    cloudBaseSize[0]+random.randint(cloudSizeOffset[0],cloudSizeOffset[1]),
                    cloudBaseSize[1]+random.randint(cloudSizeOffset[0],cloudSizeOffset[1])
                )
                )
            )
        cloudSpawnTimer = 0
        timerEnd = settings.fps*random.randint(cloudTimerOffset[0], cloudTimerOffset[1])
    else:
        cloudSpawnTimer += 1