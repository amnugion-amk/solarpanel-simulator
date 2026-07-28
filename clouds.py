import pygame
import settings
import resources
import random

spawnProbability = [1, 150]
speedProbability = [5, 10]
cloudOffset = 400

cloudBaseSize = (250, 100)
cloudSizeOffset = (-25, 45)
cloudTimerOffset = (1, 6)

maxClouds = 10
timerEnd = settings.fps*random.randint(cloudTimerOffset[0], cloudTimerOffset[1])
cloudSpawnTimer = timerEnd

class cloud:
    def __init__(self, startPos, speed, size):
        self.image = pygame.transform.scale((pygame.image.load("sprites/cloud.png").convert_alpha() ), size)
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        
        self.speed = speed
        
    def draw(self, screen):
        self.rect.x += self.speed
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