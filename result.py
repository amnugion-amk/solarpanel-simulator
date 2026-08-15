import pygame
import menus

import UIclasses
import settings
import UImanager

pygame.init()
screenDimensions = settings.size
    
def formatEfficiency(value):
    return "Efficiency: " + str(int(value)) + "%"
    
barSize = (240, 23)

resultBarObj = UIclasses.textRect(
    (menus.findCenterPos(barSize)[0], screenDimensions[1]-barSize[1]-10),
    barSize,
    (255, 255, 255),
    formatEfficiency(0)
)

UImanager.UIs.append(resultBarObj)
