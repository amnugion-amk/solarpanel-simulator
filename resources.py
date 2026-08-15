import barriers
import solar_panel

objects = []
panels = []
clouds = []
objectTrees = [clouds, objects, panels]

def remove():
    barriers.resetBarrierSettings()
    solar_panel.removePanel()
    objects.clear()
        
def removeLatestBarrier():
    if len(objects) == 0: return
    del objects[-1]
    
def removeSolarPanel():
    solar_panel.removePanel()
    
def updateObjects(screen):
    clouds[:] = [cloud for cloud in clouds if not cloud.checkOutOfBounds()]
    for objectTree in objectTrees:
        for object in objectTree:
            object.draw(screen)
                            