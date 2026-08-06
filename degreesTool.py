import pygame
import barriers
import resources

center = None
placingLineA = False
placingLineB = False

currentLineA = None
currentLineB = None

def placeCenter():
    global center
    center = pygame.mouse.get_pos()

def initializePlacingLineA():
    global placingLineA, currentLineA
    if placingLineA: return
    placingLineA = True
    mousePos = pygame.mouse.get_pos()
    currentLineA = barriers.barrier(mousePos, mousePos, color=(155, 0, 0), width=5)
    resources.invisObjects.append(currentLineA)

def whilstPlacingLineA():
    global currentLineA
    currentLineA.endPos = pygame.mouse.get_pos()

def finalizeLineA():
    global placingLineA
    placingLineA = False


def initializePlacingLineB():
    global placingLineB, currentLineB
    if placingLineB: return
    placingLineB = True
    print("set to true")
    mousePos = pygame.mouse.get_pos()
    currentLineB = barriers.barrier(mousePos, mousePos, color=(155, 0, 0), width=5)
    resources.invisObjects.append(currentLineB)

def whilstPlacingLineB():
    global currentLineB
    currentLineB.endPos = pygame.mouse.get_pos()

def finalizeLineB():
    global placingLineB
    placingLineB = False
    calcAngle()

def placeLines():
    if currentLineA == None:
        initializePlacingLineA()
    elif currentLineB == None:
        initializePlacingLineB()

def reset():
    global currentLineB, currentLineA, placingLineB, placingLineA
    currentLineB = None
    currentLineA = None

    placingLineA = False
    placingLineB = False

def calcAngle():
    A = pygame.math.Vector2(currentLineA.startPos[0], currentLineA.startPos[1])
    B = pygame.math.Vector2(currentLineA.endPos[0], currentLineA.endPos[1])
    C = pygame.math.Vector2(currentLineB.endPos[0], currentLineB.endPos[1]) # Fixed this line!

    v_ba = A - B
    v_bc = C - B

    angle = abs(v_ba.angle_to(v_bc))

    print(f"The angle ABC is: {angle} degrees")