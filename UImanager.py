import pygame

UIs = []

def drawAll(screen, events):
    for UI in UIs:
        UI.update(events, screen)