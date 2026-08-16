import pygame
import settings
import renderService
import random
import physicsObjects

physicsObjectStorage = renderService.physicsObjectsStorage

spawnProbability = [1, 150]
speedProbability = [5, 10]
cloudOffset = 250

cloudBaseSize = (250, 100)
cloudSizeOffset = (-25, 45)
cloudTimerOffset = (1, 6)

def calculatetimerEnd():
    return settings.fps*random.randint(cloudTimerOffset[0], cloudTimerOffset[1])

maxClouds = 30
timerEnd = calculatetimerEnd()
cloudSpawnTimer = timerEnd
            
def spawnCloud():
    global cloudSpawnTimer, timerEnd
    if len(physicsObjectStorage.clouds) >= maxClouds: return
    if cloudSpawnTimer >= timerEnd:
        physicsObjectStorage.clouds.append(
            physicsObjects.cloud(
                (-cloudBaseSize[0], random.randint(0, cloudOffset)),
                random.randint(speedProbability[0], speedProbability[1])/10,
                (
                    cloudBaseSize[0]+random.randint(cloudSizeOffset[0],cloudSizeOffset[1]),
                    cloudBaseSize[1]+random.randint(cloudSizeOffset[0],cloudSizeOffset[1])
                )
                )
            )
        cloudSpawnTimer = 0
        timerEnd = calculatetimerEnd()
    else:
        cloudSpawnTimer += 1