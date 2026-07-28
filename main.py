import pygame
import solar_panel
import resources
import barriers
import settings
import sun
import clouds
import controls

pygame.init()

screen = pygame.display.set_mode(settings.size)
sunObj = sun.sunClass(settings.size[0], settings.size[1])
clock = pygame.time.Clock()

controlUI = controls.controlsUI()

showingSun = False

running = True

def checkEvents():
    global running, showingSun
    for event in pygame.event.get():
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
            elif event.key == pygame.K_e and showingSun:
                showingSun = False
                print("Solar Panel Efficiency: " + str(int(sunObj.requestResults())) + "%")
                sunObj.reset()
                
                    
                    
            if event.key == pygame.K_x:
                resources.remove()

def checkConditions():
    if solar_panel.placingPanel:
        solar_panel.whilePanelPlacement(screen)
    if barriers.placingBarrier:
        barriers.whileBarrierPlacement(screen)
    
def checkSun():
    if showingSun:
        sunObj.update(screen)
        sunObj.draw(screen)   
while running:
    screen.fill(settings.background)
    checkEvents()
    checkSun()
    clouds.spawnCloud()
    resources.updateObjects(screen)
    checkConditions()
    
    
    controlUI.draw(screen)
    
    pygame.display.flip()
    clock.tick(settings.fps)
    
pygame.quit()