import math
import renderService

def checkCCW(a, b, c):
    slopeAC_numer = c[1]-a[1]
    slopeAC_denom = c[0]-a[0]
    
    slopeAB_numer = b[1]-a[1]
    slopeAB_denom = b[0]-a[0]
    
    return slopeAC_numer*slopeAB_denom > slopeAB_numer*slopeAC_denom

def checkIntersect(a, b, c, d):
    ABseparated = checkCCW(a, c, d) != checkCCW(b, c, d)
    CDseparated = checkCCW(c, a, b) != checkCCW(d, a, b)
    
    return ABseparated and CDseparated

def sineHalfCircle(yPeak, yBase, progress):
    baseDegrees = math.radians(180)
    convertPygameYaxis = yPeak-yBase
    return yBase + math.sin(baseDegrees * progress) * convertPygameYaxis

def lerp(startPos, endPos, progress):
    xPos = startPos[0]+(endPos[0]-startPos[0]) * progress
    yPos = startPos[1]+(endPos[1]-startPos[1]) * progress
    return (xPos, yPos)

def findSunPathNodes(sun, sunArcNodes, barriers, solarPanelPos=False):
    sunArcPositions = []
    sunArcNodes = 1 if sunArcNodes <= 0 else sunArcNodes
    progressIncr = 1/sunArcNodes

    yPeak = sun.yPeak
    yBase = sun.yBase

    startX = sun.startX
    endX = sun.endX

    progress = 0
    while progress < 1:
        progress += progressIncr
        
        yPos = sineHalfCircle(yPeak, yBase, progress)
        xPos = lerp((startX, yBase), (endX, yBase), progress)[0]
        
        nodePos = (xPos, yPos)
        nodeColor = (0, 220, 0)
        
        if solarPanelPos:
            for barrier in barriers:
                if checkIntersect(nodePos, solarPanelPos, barrier.startPos, barrier.endPos):
                    nodeColor = (200, 0, 0)
                    break
        
        sunArcPositions.append((xPos, yPos, nodeColor))
        
    return sunArcPositions