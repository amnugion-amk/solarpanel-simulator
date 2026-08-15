import pygame
import settings

pygame.init()
screen = pygame.display.set_mode(settings.screenSize)

import renderService
import solarPanel
import barrier

running = True
clock = pygame.time.Clock()

def checkEvents():
    global running
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                solarPanel.initPlacement()
            elif event.key == pygame.K_b:
                barrier.initPlacement()
            
            if event.key == pygame.K_s:
                solarPanel.remove()
            if event.key == pygame.K_z:
                barrier.removeLatestBarrier()
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            solarPanel.finalizePlacement()
            barrier.finalizePlacement()
    
    if solarPanel.placingPanel:
        solarPanel.whilePlacement()
    if barrier.placingBarrier:
        barrier.whilePlacement()

while running:
    checkEvents()
    renderService.renderer.renderAll(screen)
    clock.tick(settings.fps)
            
pygame.quit()