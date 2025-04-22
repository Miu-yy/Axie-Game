import pygame
from state import *
from render import *
from button import *
from ui import *

# Import tasks
view_tasks = pygame.image.load("assets/ui/tasksmenu-32x32.png")
view_tasks = pygame.transform.scale_by(view_tasks,7)
tasks_rect = pygame.Rect(16,16,224,224)

# Create checkbox buttons
empty_checkbox = Button("assets/ui/checkbox-32x32.png", 1, 0, 0, 16, 16)
checked_checkbox = Button("assets/ui/checkedbox-32x32.png", 1, 0, 0, 16, 16)

# Create arrow buttons
down_arrow = Button("assets/ui/arrow-32x32.png", 1, 0, 0, 16, 16)
up_arrow = Button("assets/ui/uparrow-32x32.png", 1, 0, 0, 16, 16)



def task_page(window,player):
    tasks = player.tasks
    num_tasks = player.num_tasks()

def render_tasks_tab(window,tasks):
    window.blit(view_tasks,tasks_rect)
    num_tasks = 0
    for task in tasks:
        num_tasks += 1
        y = 32 + 16*num_tasks
        if not task["completed"]:
            empty_checkbox.draw(window)
            render_font(window, (0,0,0), task["title"], 20, 32, y)
            render_font(window, (0,255,0), str(task["value"]), 20, 192, y)
    num_tasks = 0
    for task in tasks:
        num_tasks += 1
        y = 192 - 16*num_tasks
        if task["completed"]:
            render_font(window, (0,0,0), task["title"], 20, 32, y)
            render_font(window, (0,255,0), str(task["value"]), 20, 192, y)