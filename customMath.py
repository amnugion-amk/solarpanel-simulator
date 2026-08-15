import math

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