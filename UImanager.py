import pygame

menus = []
buttons = []
background = None

UIs = [buttons, menus]

def drawAll(screen, events):
    for UI in UIs:
        for UIobj in UI:
            UIobj.update(events, screen)