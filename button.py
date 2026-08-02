import pygame
import controls
import settings
import resources
import sun
import UIclasses

screenDinmensions = settings.size

        
def onPressedControlsButton():
    print("pressed!")
    controls.controlsUIObj.enabled = not controls.controlsUIObj.enabled
    
def onPressedDeleteAllButton():
    resources.remove()
    
def onPressedHelp():
    controls.helpUIObj.enabled = not controls.helpUIObj.enabled
def onPressedBegin():
    if not sun.showingSun:
        sun.showingSun = True
    elif sun.showingSun and sun.sunObj.progress >= 1:
        sun.sunObj.reset()
        sun.showingSun = True
   
size = (80, 23)
posOffsets = (5, -10)
    
controlsButton = UIclasses.button(
    "Controls",
    (0+posOffsets[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    size,
    onPressedControlsButton,
    (225, 225, 225),
    (255, 255, 255)    
)

deleteAll = UIclasses.button(
    "Delete All",
    (0+posOffsets[0]*2+size[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    size,
    onPressedDeleteAllButton,
    (225, 225, 225),
    (255, 255, 255) 
)

helpButton = UIclasses.button(
    "?",
    (0+posOffsets[0]*3+size[0]*2, screenDinmensions[1]-size[1]+posOffsets[1]),
    (25, 23),
    onPressedHelp,
    (225, 225, 225),
    (255, 255, 255) 
)

beginButton = UIclasses.button(
    "Begin",
    (screenDinmensions[0]-size[0], screenDinmensions[1]-size[1]+posOffsets[1]),
    (75, 23),
    onPressedBegin,
    (225, 225, 225),
    (255, 255, 255) 
)