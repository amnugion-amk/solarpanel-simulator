import pygame
activeUIs = []

def drawAll():
    for UI in activeUIs:
        UI.draw()