import sys
import pygame
import settings

pygame.init()

resultFont = pygame.font.Font(None, 40)
text_obj = resultFont.render("placeholder", True, (0, 0, 0))
text_objRect = text_obj.get_rect()
text_objRect.center = (settings.size[0]/2, settings.size[1]-text_obj.get_height())

def drawText(text, screen):
    text_obj = resultFont.render(text, True, (0, 0, 0))
    screen.blit(text_obj, text_objRect)