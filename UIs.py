import pygame
import settings
import physicsObjects
import renderService
import UIClasses
import result

screenDinmensions = settings.screenSize
UIObjectsStorage = renderService.UIObjectsStorage
physicsObjectsStorage = renderService.physicsObjectsStorage

sun = physicsObjectsStorage.sun[0]

def findCenterPos(size):
    return (screenDinmensions[0]/2-size[0]/2, screenDinmensions[1]/2-size[1]/2)

controlsUISize = (320, 250)
controlsUIPos = findCenterPos(controlsUISize)

helpUISize = (760, 600)
helpUIPos = findCenterPos(helpUISize)

controlsUIObj = UIClasses.imageUI(controlsUIPos, controlsUISize, (255, 255, 255), "sprites/controls.png", controlsUISize)
helpUIObj = UIClasses.imageUI(helpUIPos, helpUISize, (255, 255, 255), "sprites/help.png", helpUISize)

UIObjectsStorage.menus.append(controlsUIObj)
UIObjectsStorage.menus.append(helpUIObj)
        
def findBottomYPosition(size, offset):
    return screenDinmensions[1]-size[1]-offset
        
def onPressedControlsButton():
    controlsUIObj.enabled = not controlsUIObj.enabled
    
def onPressedDeleteAllButton():
    physicsObjectsStorage.destroyAll()
    
def onPressedHelp():
    helpUIObj.enabled = not helpUIObj.enabled
    
def onPressedBegin():
    if sun.showingSun:
        sun.endCycle()
    else:
        sun.showingSun = True
    beginButton.updateImg()
   
def onPressedPause():
    sun.paused = not sun.paused   

size = (80, 23)
posOffsets = (5, 10)
    
controlsButton = UIClasses.button(
    "Kontrols",
    (posOffsets[0], findBottomYPosition(size, posOffsets[1])),
    size,
    onPressedControlsButton,
    (225, 225, 225),
    (255, 255, 255)    
)
UIObjectsStorage.buttons.append(controlsButton)

deleteAllSize = (130, 23)
deleteAllButton = UIClasses.button(
    "Hapus Semua",
    (posOffsets[0]*2+size[0], findBottomYPosition(size, posOffsets[1])),
    deleteAllSize,
    onPressedDeleteAllButton,
    (225, 225, 225),
    (255, 255, 255) 
)
UIObjectsStorage.buttons.append(deleteAllButton)
helpButton = UIClasses.button(
    "?",
    (posOffsets[0]*6+((deleteAllSize[0])*1.5), findBottomYPosition(size, posOffsets[1])),
    (25, 23),
    onPressedHelp,
    (225, 225, 225),
    (255, 255, 255) 
)
UIObjectsStorage.buttons.append(helpButton)

beginButton = UIClasses.beginSunButton(
    "sprites/play.png",
    (screenDinmensions[0]-25-posOffsets[0], findBottomYPosition(size, posOffsets[1])),
    (25, 23),
    onPressedBegin,
    (225, 225, 225),
    (255, 255, 255) 
)
UIObjectsStorage.buttons.append(beginButton)

pauseButton = UIClasses.buttonImg(
    "sprites/pause.png",
    (screenDinmensions[0]-50-posOffsets[0]*2, findBottomYPosition(size, posOffsets[1])),
    (25, 23),
    onPressedPause,
    (225, 225, 225),
    (255, 255, 255) 
)
UIObjectsStorage.buttons.append(pauseButton)