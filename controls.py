import pygame
import settings
import UIclasses

screenDimensions = settings.size



controlsUISize = (320, 250)
controlsUIPos = (screenDimensions[0]/2-controlsUISize[0]/2,screenDimensions[1]/2-controlsUISize[1]/2) 

helpUISize = (760, 600)
helpUIPos = (screenDimensions[0]/2-helpUISize[0]/2,screenDimensions[1]/2-helpUISize[1]/2) 

controlsUIObj = UIclasses.imageUI(controlsUIPos, controlsUISize, (255, 255, 255), "sprites/controls.png", controlsUISize)
helpUIObj = UIclasses.imageUI(helpUIPos, helpUISize, (255, 255, 255), "sprites/help.png", helpUISize)