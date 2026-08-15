import settings
import UIclasses
import UImanager

screenDimensions = settings.size
def findCenterPos(size):
    return (screenDimensions[0]/2-size[0]/2, screenDimensions[1]/2-size[1]/2)

controlsUISize = (320, 250)
controlsUIPos = findCenterPos(controlsUISize)

helpUISize = (760, 600)
helpUIPos = findCenterPos(helpUISize)

controlsUIObj = UIclasses.imageUI(controlsUIPos, controlsUISize, (255, 255, 255), "sprites/controls.png", controlsUISize)
helpUIObj = UIclasses.imageUI(helpUIPos, helpUISize, (255, 255, 255), "sprites/help.png", helpUISize)

UImanager.UIs.append(controlsUIObj)
UImanager.UIs.append(helpUIObj)