import pygame
import settings

class textLabel():
    def __init__(self, fontSize, color, text, anchorPoint):
        self.font = pygame.font.Font(None, fontSize)
        self.currentColor = color
        self.currentText = text
        
        self.textSurface = self.font.render(self.currentText, True, self.currentColor)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = anchorPoint
        self.previousText = None
        
    def draw(self, screen):
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
        self.textLabel.draw(screen)
    def update(self, events, screen):
        mousePos = pygame.mouse.get_pos()
        isColliding = self.rect.collidepoint(mousePos)
        
        self.draw(screen, isColliding)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isColliding:
                self.onPressed()
        
class basicUI:
    def __init__(self, pos, size, color, radius=2):
        self.currentSize = size
        self.currentPos = pos
        
        self.currentColor = color
        self.radius = radius
        
        self.rect = None
        self.updateRect(pos, size)
        
        self.enabled = True
        self.hasExit = True
        
        
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
        
        
    def update(self, events, screen):
        if not self.enabled: return
        self.updateRect(self.currentPos, self.currentSize)
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        if self.hasExit: self.exitButton.update(events, screen)

class imageUI(basicUI):
    def __init__(self, pos, size, color, image, imageSize, radius=2):
        super().__init__(pos, size, color, radius)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), imageSize)
        self.updateRect(
            pos,
            (self.image.get_width(), self.image.get_height())
        )
    def update(self, events, screen):
        if not self.enabled: return
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        screen.blit(self.image, self.rect)
        self.exitButton.update(events, screen)
        
class textRect(basicUI):
    def __init__(self, pos, size, color, text, fontSize = 24, fontColor = (0, 0, 0), radius=2):
        super().__init__(pos, size, color, radius)
        self.exitButton = None
        self.textLabel = textLabel(fontSize, fontColor, text, self.rect.center)
        
    def update(self, events, screen):
        if not self.enabled: return
        self.updateRect(self.currentPos, self.currentSize)
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=self.radius)
        self.textLabel.draw(screen)
        
class backgroundUI():
    def __init__(self, image):
        self._currentImage = pygame.transform.scale(pygame.image.load(image), settings.size).convert_alpha()
        self.enabled = True
        
        self.rect = self._currentImage.get_rect()
    
    def changeBackground(self, image):
        self._currentImage = pygame.transform.scale(pygame.image.load(image), settings.size).convert_alpha()
    
    def update(self, screen):
        if not self.enabled: return
        screen.blit(self._currentImage, self.rect)
class checkboxUI(button):
    def __init__(self, pos, size, checkboxName, colorOnHover=(225, 225, 225), colorNormal=(255, 255, 255)):
        super().__init__(" ", pos, size, self.switch, colorOnHover, colorNormal)
        self.ticked = False
        self.onPressed = self.switch
        
        self.rect.height = 18
        self.textLabel.textRect.height
        
        self.checkboxTitle = textLabel(24, (0, 0, 0), checkboxName, (0, 0))
        self.mainRectSize = (
            self.checkboxTitle.textRect.width+size[0],
            18
        ) 
        
        self.mainRect = basicUI(pos, self.mainRectSize, (255, 255, 255))
        self.checkboxTitle.textRect.center = (
            self.mainRect.rect.x+self.checkboxTitle.textRect.width/2,
            self.mainRect.rect.y+self.checkboxTitle.textRect.height/2
        )
        
        self.rect.x = self.checkboxTitle.textRect.centerx+self.checkboxTitle.textRect.width/2
        self.rect.y = pos[1]
        
        self.mainRect.hasExit = False
        
        self.textLabel.textRect.center = self.rect.center
        
    
    def switch(self):
        self.ticked = not self.ticked
        self.textLabel.currentText = "O" if self.ticked else " "
        
    def update(self, events, screen):
            mousePos = pygame.mouse.get_pos()
            isColliding = self.rect.collidepoint(mousePos)
            
            self.mainRect.update(events, screen)
            self.draw(screen, isColliding)
            self.checkboxTitle.draw(screen)
            
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isColliding:
                    self.onPressed()
