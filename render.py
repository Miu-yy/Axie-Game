import pygame
from sprites import *
import interactable,tasks

# Import background
tank = pygame.image.load("tank-32x32.png")
tank = pygame.transform.scale_by(tank,16)

# Import tasks TEMP
view_tasks = pygame.image.load("tasksmenu-32x32.png")
view_tasks = pygame.transform.scale_by(view_tasks,7)
tasks_rect = pygame.Rect(16,16,224,224)


# Draw background
def background(window):
    location = pygame.math.Vector2(0,0)
    sprite = pygame.Rect(0,256,512,256)
    window.blit(tank,location,sprite)

def render(window):
    background(window)
    mo.draw(window)
    stumpy.draw(window)
    decorations.draw(window)

def tasks_tab(window):
    window.blit(view_tasks,tasks_rect)

# Groups
mo = pygame.sprite.GroupSingle()
mo.add(Mo())
stumpy = pygame.sprite.GroupSingle()
stumpy.add(Stumpy())
decorations = pygame.sprite.Group()
decorations.add(Decorations('log',2))

# Buttons
tasks_little = interactable.Button("tasks-32x32.png",1,16,16,128,76)
tasks_button = interactable.Button("tasks-32x32.png",4,16,16,128,76)
tasks = False
#tasksButton.draw(window)