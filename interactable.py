import pygame

class Button():
    def __init__(self,image,x,y,width,height):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(image,8)
        self.rect = pygame.Rect(x,y,width,height)

    def draw(self,window,location):
        window.blit(self.image,self.rect)