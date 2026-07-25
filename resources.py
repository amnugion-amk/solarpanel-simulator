import barriers
import solar_panel

objects = []
panels = []
objectTrees = [objects, panels]

def remove():
    barriers.removeBarrier()
    solar_panel.removePanel()
    
    for objectTree in objectTrees:
        objectTree.clear()
        
def removeLatestBarrier():
    if len(objects) == 0: return
    del objects[-1]
    
def removeSolarPanel():
    solar_panel.removePanel()
    
def updateObjects(screen):
    for objectTree in objectTrees:
        for object in objectTree:
            object.draw(screen)