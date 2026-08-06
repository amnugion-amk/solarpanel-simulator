import barriers
import solar_panel
import degreesTool

objects = []
invisObjects = []
panels = []
clouds = []
objectTrees = [clouds, objects, panels, invisObjects]

def remove():
    barriers.removeBarrier()
    solar_panel.removePanel()
    invisObjects.clear()
    degreesTool.reset()
    objects.clear()
        
def removeLatestBarrier():
    if len(objects) == 0: return
    del objects[-1]
    
def removeSolarPanel():
    solar_panel.removePanel()
    
def updateObjects(screen):
    global clouds
    clouds[:] = [cloud for cloud in clouds if not cloud.checkOutOfBounds()]
    for objectTree in objectTrees:
        for object in objectTree:
            object.draw(screen)
                            