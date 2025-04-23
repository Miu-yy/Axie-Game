import pygame

class Button():
    def __init__(self,image,scale,x,y,width,height):
        self.scale = scale
        self.width = width
        self.height = height

        image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(image,scale)
        self.rect = pygame.Rect(x,y,width,height)
        self.hover = False

    def place_button(self,x,y):
        self.rect = pygame.Rect(x,y,self.width,self.height)

    def change_image(self,image):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale_by(image,self.scale)

    def draw_hover(self,window,mouse_position=(0,0),mouse_clicked=False):
        window.blit(self.image,self.rect)
        if self.rect.collidepoint(mouse_position):
            self.hover = True
            return True
        else:
            return False

    def draw_click(self,window,mouse_position=(0,0),mouse_clicked=False):
        window.blit(self.image, self.rect)
        if self.rect.collidepoint(mouse_position) and mouse_clicked:
            return True
        else:
            return False
