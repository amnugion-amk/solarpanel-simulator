import pygame
import renderService
import settings
import customMath
import result

screenSize = settings.screenSize
physicsObjectStorage = renderService.physicsObjectsStorage
showingNodes = False

class line():
    def __init__(self, startPos, endPos, color, width):
        self.startPos = startPos
        self.endPos = endPos
        self.prevPositions = (self.startPos, self.endPos)
        
        self.transparency = 75
        self.color = color
        
        self.width = width
        
        self.currentScreen = renderService.renderer.transparentSurface
        
        self.centerPos = customMath.lerp(startPos, endPos, 0.5)
    def checkForChanges(self):
        currStart = self.startPos
        currEnd = self.endPos
        
        currPos = (currStart, currEnd)
        
        if self.prevPositions == currPos: return
        self.centerPos = customMath.lerp(currStart, currEnd, 0.5)
        self.prevPositions = currPos
        
    def revertTransparency(self):
        self.transparency = 255
        self.currentScreen = settings.screen
        
    def render(self, screen):
        self.checkForChanges()
        pygame.draw.line(self.currentScreen, (self.color[0], self.color[1], self.color[2], self.transparency), self.startPos, self.endPos, self.width)
        
class sun():
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/sun.png").convert_alpha(),
            (200, 200)
        )
        
        self.rect = self.image.get_rect()
        self.paused = False
        
        self.yPeak = 0
        self.yBase = screenSize[1]
        
        self.startX = screenSize[0]
        self.endX = 0
        
        self.progress = 0
        self.speed = 0.003
        
        self.showingSun = False
        
        self.blocked = 0
        self.total = 0
        
        self.resetPos()
         
    def render(self, screen):
        if not self.showingSun: return
        if self.progress == 0:
            self.paused = False
        
        if self.progress < 1:
            if not self.paused:
                self.rect.centerx = customMath.lerp((self.startX, self.yBase), (self.endX, self.yBase), self.progress)[0]
                self.rect.centery = customMath.sineHalfCircle(self.yPeak, self.yBase, self.progress)
                self.progress += self.speed
            
            if len(physicsObjectStorage.solarPanel) != 1: self.draw(screen); return
            solarPanel = physicsObjectStorage.solarPanel[0]
            rayColor = (0, 255, 0)
            
            sunCenter = self.rect.center
            solarPanelCenter = solarPanel.centerPos
            
            for barrier in physicsObjectStorage.barriers:
                if customMath.checkIntersect(sunCenter, solarPanelCenter, barrier.startPos, barrier.endPos):
                    rayColor = (255, 0, 0)
                    self.blocked += 1 if not self.paused else 0
                    break
                
            self.total += 1 if not self.paused else 0
            
            pygame.draw.line(screen, rayColor, sunCenter, solarPanelCenter, 5)
            self.draw(screen)
        else:
            self.endCycle()
            
    def endCycle(self):
        self.progress = 0
        self.showingSun = False
        
        result.resultBarObj.textLabel.currentText = result.formatResults(self.requestResults())
        self.paused = False
        
        self.total = 0
        self.blocked = 0
        
        self.resetPos()
        
    def resetPos(self):
        self.rect.x = self.startX
        self.rect.y = self.yBase
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def requestResults(self):
        absorbed = self.total-self.blocked
        return absorbed/self.total*100 if self.total != 0 else 0
    
physicsObjectStorage.sun.append(sun())

class cloud:
    def __init__(self, startPos, speed, size):
        self.image = pygame.transform.scale((pygame.image.load("sprites/cloud.png").convert_alpha() ), size)
        self.rect = self.image.get_rect()
        
        self.currentXpPosition = float(startPos[0])
        
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        
        self.putInsideDeleteList = False
        
        self.speed = speed
        
    def render(self, screen):
        self.currentXpPosition += self.speed
        self.rect.x = int(self.currentXpPosition)
        screen.blit(self.image, self.rect)
        if self.checkOutOfBounds() and not self.putInsideDeleteList:
            self.putInsideDeleteList = True
            physicsObjectStorage.cloudsDeleteList.append(self)
            
    def checkOutOfBounds(self):
            if self.rect.x > settings.screenSize[0]:
                return True
            return False
        
class sunNodes():
    def __init__(self, color, pos, radius, width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
    
    def render(self, screen):
        if not showingNodes: return
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.width)
    
prevBarriers = []
prevSolarPanel = []

def formatLineListforNodes(lineList):
    newList = []
    for placedLine in lineList:
        newList.append(
            (placedLine.startPos, placedLine.endPos)
        )
    return newList

def findSolarPanelPos():
    return physicsObjectStorage.solarPanel[-1].centerPos if len(physicsObjectStorage.solarPanel)==1 else False    

def createNewNodes(solarPanelPos):
    physicsObjectStorage.sunNodes.clear()
    sunArchNodes = customMath.findSunPathNodes(
        physicsObjectStorage.sun[-1],
        50,
        physicsObjectStorage.barriers,
        solarPanelPos
    )
            
    for nodeInfo in sunArchNodes:
        physicsObjectStorage.sunNodes.append(sunNodes(
            nodeInfo[2],
            (nodeInfo[0], nodeInfo[1]),
            5,
            3    
            )
        )

def checkForPlacementDifferences():
    global prevSolarPanel, prevBarriers
    
    if formatLineListforNodes(physicsObjectStorage.barriers) != prevBarriers or formatLineListforNodes(physicsObjectStorage.solarPanel) != prevSolarPanel:
        prevBarriers = formatLineListforNodes(physicsObjectStorage.barriers)
        prevSolarPanel = formatLineListforNodes(physicsObjectStorage.solarPanel)
        createNewNodes(findSolarPanelPos())
        
createNewNodes(findSolarPanelPos())