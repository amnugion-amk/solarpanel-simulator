import pygame

class sunClass():
    def __init__(self, screenWidth, screenHeight):
        self.width = screenWidth
        self.height = screenHeight
        self.image = pygame.transform.scale(
            pygame.image.load("sprites/sun.png").convert_alpha(),
            (150, 150)
        )
        self.rect = self.image.get_rect()
        self.startX = screenWidth
        self.endX = 0
        
        self.startY = screenHeight/2
        self.endY = screenHeight/2
        
        self.yPeak = screenHeight/2
        
        self.progress = 0
        self.speed = 0.005
        
    def update(self):
        if self.progress <= 1:
            currX = self.startX + (self.endX-self.startX) * self.progress
            currY = self.startY + (self.endY-self.startY) * self.progress
            
            currY += -4 * self.yPeak * self.progress * (1 - self.progress)
            
            self.rect.x = currX
            self.rect.y = currY
            
            self.progress += self.speed
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def reset(self):
        self.progress = 0
        