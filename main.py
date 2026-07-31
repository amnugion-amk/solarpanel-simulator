import pygame
import settings

pygame.init()

screen = pygame.display.set_mode(settings.size)

import solar_panel
import resources
import barriers
import sun
import clouds
import result
import button
import controls

sunObj = sun.sunClass(settings.size[0], settings.size[1])
clock = pygame.time.Clock()

showingSun = False
showingResult = False

running = True

def checkEvents(events):
    global running, showingSun, showingResult
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not solar_panel.placingPanel and len(resources.panels)<1:
                solar_panel.initiatePanelPlacement()
            elif event.key == pygame.K_r and solar_panel.placingPanel and len(resources.panels)<1:
                solar_panel.finalizePanelPlacement(solar_panel.currentPanel)
                
                
            if event.key == pygame.K_b and not barriers.placingBarrier:
                barriers.initiateBarrierPlacement()
            elif event.key == pygame.K_b and barriers.placingBarrier:
                barriers.finalizeBarrierPlacement()
                
                
            if event.key == pygame.K_z:
                resources.removeLatestBarrier()
                
            if event.key == pygame.K_s:
                resources.removeSolarPanel()
                
                
            if event.key == pygame.K_e and not showingSun:
                showingSun = True
            elif event.key == pygame.K_e and showingSun and sunObj.progress >= 1:
                showingSun = False
                
                sunObj.reset()
                showingResult = False
                
            if event.key == pygame.K_x:
                resources.remove()

        
def checkConditions():
    if solar_panel.placingPanel:
        solar_panel.whilePanelPlacement(screen)
    if barriers.placingBarrier:
        barriers.whileBarrierPlacement(screen)
    if sunObj.progress >= 1:
        result.drawText("Solar Panel Efficiency: " + str(int(sunObj.requestResults())) + "%", screen)

    
def checkSun():
    if showingSun:
        sunObj.update(screen)
        sunObj.draw(screen)   
while running:
    currentEvents = pygame.event.get()
    
    screen.fill(settings.background)
    
    checkEvents(currentEvents)
    checkSun()
    clouds.spawnCloud()
    resources.updateObjects(screen)
    checkConditions()
    
    button.controlsButton.update(currentEvents, screen)
    button.simulationButton.update(currentEvents, screen)
    button.helpButton.update(currentEvents, screen)
    button.beginButton.update(currentEvents, screen)
    
    controls.controlsUIObj.draw(screen)
    result.resultBarObj.draw(screen)
    result.textObj.draw(screen)
    
    pygame.display.flip()
    clock.tick(settings.fps)
    
pygame.quit()