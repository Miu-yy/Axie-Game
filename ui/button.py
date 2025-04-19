import pygame

class Button():
    def __init__(self,image,scale,x,y,width,height):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(image,scale)
        self.rect = pygame.Rect(x,y,width,height)

    def draw(self,mousePosition,window):
        window.blit(self.image,self.rect)
        if self.rect.collidepoint(mousePosition):
            return True
        else:
            return False