import pygame

# Import background
tank = pygame.image.load("assets/background/tank-32x32.png")
tank = pygame.transform.scale_by(tank,16)

# Import sprites
sprites = pygame.image.load("assets/sprites/sprites-32x32.png")
sprites = pygame.transform.scale_by(sprites, 8)

# Import tasks menu
view_tasks = pygame.image.load("assets/ui/tasksmenu-32x32.png")
view_tasks = pygame.transform.scale_by(view_tasks,7)
tasks_rect = pygame.Rect(16,16,224,224)

# Import buy menu


# Import placement overlay


class Mo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,0,152,48)
        self.image = sprites.subsurface(self.rect)
        #self.rect.topleft = (32,32)
        pygame.Rect.update(self.rect,256,32,0,0)


class Stumpy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0,64,152,48)
        self.image = sprites.subsurface(self.rect)
        #self.rect.topleft = (256,176)
        pygame.Rect.update(self.rect,288,176,0,0)


class Decorations(pygame.sprite.Sprite):
    def __init__(self,item,level):
        super().__init__()

        if item == 'log':
            self.rect = pygame.Rect(0,128,168,48)
            self.image = sprites.subsurface(self.rect)
            #self.rect.topleft = ()
            pygame.Rect.update(self.rect,128,184,0,0)

        elif item == 'rock':
            self.rect = pygame.Rect(192,144,48,32)
            self.image = sprites.subsurface(self.rect)
            #self.rect.topleft = ()
            pygame.Rect.update(self.rect,240,192,0,0)

        elif item == 'weed':
            self.rect = pygame.Rect(level*8*3,192,16,64) # x=(every 3 pixels),y=24,w=2,h=8, assume all are 8 tall and start at 24
            self.image = sprites.subsurface(self.rect)
            #self.rect.topleft = ()
            pygame.Rect.update(self.rect,240,160,0,0)

        elif item == 'flower':
            self.rect = pygame.Rect((15+level*5)*8,208,(2+int(level*2.5))*8,48) # x=17,y=26,w=7,h=6
            self.image = sprites.subsurface(self.rect)
            #self.rect.topleft = ()
            pygame.Rect.update(self.rect,184,176,0,0)


mo = pygame.sprite.GroupSingle()
mo.add(Mo())
stumpy = pygame.sprite.GroupSingle()
stumpy.add(Stumpy())
decorations = pygame.sprite.Group()
decorations.add(Decorations('log',2))