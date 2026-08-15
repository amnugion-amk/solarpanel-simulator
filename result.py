import pygame
import UIClasses
import settings
import renderService

UIObjectsStorage = renderService.UIObjectsStorage

screenDimensions = settings.screenSize

def formatResults(result):
    return "Effisiensi: " + str(int(result)) + "%"
def findCenterPos(size):
    return (screenDimensions[0]/2-size[0]/2, screenDimensions[1]/2-size[1]/2)

barSize = (240, 23)

resultBarObj = UIClasses.textRect(
    (findCenterPos(barSize)[0], screenDimensions[1]-barSize[1]-10),
    barSize,
    (255, 255, 255),
    formatResults(0)
)
UIObjectsStorage.texts.append(resultBarObj)

