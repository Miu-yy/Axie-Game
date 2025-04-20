import pygame

class Button():
    def __init__(self,image,scale,x,y,width,height):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(image,scale)
        self.rect = pygame.Rect(x,y,width,height)
        self.hover = False

    def draw(self,window,mouse_position=(0,0)):
        window.blit(self.image,self.rect)
        if self.rect.collidepoint(mouse_position):
            self.hover = True
            return True
        else:
            return False