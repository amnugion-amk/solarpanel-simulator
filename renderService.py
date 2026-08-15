import pygame
import settings

bgColor = settings.backgroundColor

class rendererClass():
    def __init__(self, objectStorages):
        self.objectStorages = objectStorages
        
    def renderAll(self, screen):
        screen.fill(bgColor)
        
        for objectStorage in self.objectStorages:
            objectStorage.render(screen)
            
        pygame.display.flip()    
        
class objectStorage_SuperClass():
    def __init__(self):
        self.renderQueue = []
        
    def render(self, screen):
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
        
class physicsObjects(objectStorage_SuperClass):
    def __init__(self):
        super().__init__()
        self.barriers = []
        self.clouds = []
        self.solarPanel = []
        self.sun = []
        
        self.renderQueue = [self.sun, self.clouds, self.barriers, self.solarPanel]

UIObjectsStorage = UIObjects()
physicsObjectsStorage = physicsObjects()

renderer = rendererClass([physicsObjectsStorage, UIObjectsStorage])