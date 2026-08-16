import pygame
import settings
import renderService

class textLabel():
    def __init__(self, fontSize, color, text, pos):
        self.font = pygame.font.Font(None, fontSize)
        self.currentColor = color
        self.currentText = text

        self.textSurface = self.font.render(self.currentText, True, self.currentColor)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = pos
        self.previousText = None
        
    def render(self, screen):
        if self.currentText != self.previousText:
            self.textSurface = self.font.render(self.currentText, True, self.currentColor)
            self.previousText = self.currentText
        screen.blit(self.textSurface, self.textRect)

class button():
    def __init__(self, textString, pos, size, onPressed, colorOnHover, colorNormal):
        self.colorOnHover = colorOnHover
        self.colorNormal = colorNormal
        
        self.pos = pos
        self.size = size
        
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.onPressed = onPressed
        
        self.currentColor = self.colorNormal
        
        self.textString = textString
        self.textLabel = textLabel(24, (0, 0, 0,), self.textString, self.rect.center)        
        
        
    def draw(self, screen, isColliding):
        self.currentColor = self.colorOnHover if isColliding else self.colorNormal
        
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=2)
        self.textLabel.render(screen)
    def render(self, screen, events):
        mousePos = pygame.mouse.get_pos()
        isColliding = self.rect.collidepoint(mousePos)
        
        self.draw(screen, isColliding)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isColliding:
                self.onPressed()
    
class buttonImg(button):
    def __init__(self, image, pos, size, onPressed, colorOnHover, colorNormal, textString=""):
        super().__init__(textString, pos, size, onPressed, colorOnHover, colorNormal)
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
        self.imageRect = self.image.get_rect()
        self.imageRect.center = self.rect.center
        
    def draw(self, screen, isColliding):
        self.currentColor = self.colorOnHover if isColliding else self.colorNormal
            
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=2)
        screen.blit(self.image, self.imageRect)
    
    def changeImage(self, newImg):
        self.image = pygame.transform.scale(pygame.image.load(newImg).convert_alpha(), self.size)
        
class beginSunButton(buttonImg):
    def __init__(self, image, pos, size, onPressed, colorOnHover, colorNormal, textString=""):
        super().__init__(image, pos, size, onPressed, colorOnHover, colorNormal, textString)
        self.playImg = "sprites/play.png"
        self.endImg = "sprites/stop.png"
        
        self.currentImg = self.playImg
        
        self.sun = renderService.physicsObjectsStorage.sun[-1]
    def render(self, screen, events):
        if not self.sun.showingSun and self.currentImg == self.endImg:
            self.changeImage(self.playImg)
            self.currentImg = self.playImg
            
        mousePos = pygame.mouse.get_pos()
        isColliding = self.rect.collidepoint(mousePos)
                
        self.draw(screen, isColliding)
                
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isColliding:
                self.onPressed()
            
    def updateImg(self):
        if self.sun.showingSun == True:
            self.changeImage(self.endImg)
            self.currentImg = self.endImg
        else:
            self.changeImage(self.playImg)
            self.currentImg = self.playImg
            
        
class basicUI:
    def __init__(self, pos, size, color, radius=2):
        self.currentColor = color
        self.radius = radius
        
        self.rect = (
            pos[0],
            pos[1],
            size[0],
            size[1]
        )
        
        self.enabled = True
        self.exitButton = button("X", self.rect, (15, 15), self.exitUI, (225, 225, 225), (255, 255, 255))
        
    def updateRect(self, pos, size):
        self.rect = pygame.Rect(
            pos[0],
            pos[1],
            size[0],
            size[1]
        )

    def exitUI(self):
        self.enabled = False
        
        
    def render(self, screen, events):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        self.exitButton.render(screen, events)

class imageUI(basicUI):
    def __init__(self, pos, size, color, image, imageSize, radius=2):
        super().__init__(pos, size, color, radius)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), imageSize)
        self.rect = (
            pos[0],
            pos[1],
            self.image.get_width(),
            self.image.get_height()
        )
    def render(self, screen, events):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        screen.blit(self.image, self.rect)
        self.exitButton.render(screen, events)
        
class textRect(basicUI):
    def __init__(self, pos, size, color, text, fontSize = 24, fontColor = (0, 0, 0), radius=2):
        super().__init__(pos, size, color, radius)
        self.exitButton = None
        self.rect = pygame.Rect(
            pos[0],
            pos[1],
            size[0],
            size[1]
        )
        
        self.textLabel = textLabel(fontSize, fontColor, text, self.rect.center)
        
    def render(self, screen, events):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        self.textLabel.render(screen)