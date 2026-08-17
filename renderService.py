import pygame
import settings

bgColor = settings.backgroundColor

class rendererClass():
    def __init__(self, objectStorages):
        self.objectStorages = objectStorages
        self.transparentSurface = pygame.Surface((settings.screenSize), pygame.SRCALPHA)
        
    def renderAll(self, screen, events):
        screen.fill(bgColor)
        screen.blit(self.transparentSurface, (0, 0))
        self.transparentSurface.fill(bgColor)
        
        for objectStorage in self.objectStorages:
            objectStorage.render(screen, events)
            
        pygame.display.flip()    
        
class objectStorage_SuperClass():
    def __init__(self):
        self.renderQueue = []
        
    def render(self, screen, events):
        for objectType in self.renderQueue:
            if isinstance(objectType, list):
                for object in objectType:
                    object.render(screen)

class UIObjects(objectStorage_SuperClass):
    def __init__(self):
        super().__init__()
        self.menus = []
        self.buttons = []
        self.texts = []  
        self.renderQueue = [self.menus, self.texts, self.buttons]
        
    def render(self, screen, events):
            for objectType in self.renderQueue:
                if isinstance(objectType, list):
                    for object in objectType:
                        object.render(screen, events)
        
class physicsObjects(objectStorage_SuperClass):
    def __init__(self):
        super().__init__()
        self.barriers = []
        self.solarPanel = []
        self.sun = []
        
        self.sunNodes = []
        
        self.clouds = []
        self.cloudsDeleteList = []
        
        self.renderQueue = [self.sun, self.clouds, self.sunNodes, self.barriers, self.solarPanel]
        
    def destroyAll(self):
        self.barriers.clear()
        self.solarPanel.clear()
        
    def render(self, screen, events):
                for cloud in self.cloudsDeleteList:
                    if not cloud in self.clouds: continue
                    self.clouds.remove(cloud)

                for objectType in self.renderQueue:
                    if isinstance(objectType, list):
                        for object in objectType:
                            object.render(screen)

UIObjectsStorage = UIObjects()
physicsObjectsStorage = physicsObjects()

renderer = rendererClass([physicsObjectsStorage, UIObjectsStorage])