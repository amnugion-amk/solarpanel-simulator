import pygame
import settings

pygame.init()

screen = pygame.display.set_mode(settings.size)

import solar_panel
import resources
import barriers
import sun
import clouds
import UImanager
import button

clock = pygame.time.Clock()

showingResult = False
running = True

def checkEvents(events):
    global running, showingResult
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and not solar_panel.placingPanel and len(resources.panels)<1:
                solar_panel.initiatePanelPlacement()                    
            if event.key == pygame.K_b and not barriers.placingBarrier:
                barriers.initiateBarrierPlacement()
                
            if event.key == pygame.K_z:
                resources.removeLatestBarrier()
            if event.key == pygame.K_s:
                resources.removeSolarPanel()
                
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if solar_panel.placingPanel and len(resources.panels) < 1:
                solar_panel.finalizePanelPlacement()
            if barriers.placingBarrier:
                barriers.finalizeBarrierPlacement()

        
def checkConditions():
    if solar_panel.placingPanel:
        solar_panel.whilePanelPlacement(screen)
    if barriers.placingBarrier:
        barriers.whileBarrierPlacement(screen)

    
def checkSun():
    if sun.showingSun:
        sun.sunObj.update(screen)
        sun.sunObj.draw(screen)   
while running:
    currentEvents = pygame.event.get()
    
    screen.fill(settings.background)
    
    checkEvents(currentEvents)
    checkSun()
    clouds.spawnCloud()
    resources.updateObjects(screen)
    checkConditions()
    
    UImanager.drawAll(screen, currentEvents)
    
    pygame.display.flip()
    clock.tick(settings.fps)
    
pygame.quit()