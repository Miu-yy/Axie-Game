import pygame
import render

#view_tasks = pygame.image.load("tasksmenu-32x32.png")
#tasks_rect = pygame.Rect(0,0,32,32)

def check():
    pass
    # if hover_little:
    #     if hover_button and mouse_click:
    #         tasks = True
    # else:
    #     pass

def render_tasks(window,tasks,mouse_pos,mouse_click):
    #tasks = False
    hover_little = False
    if not tasks:
        hover_little = render.tasks_little.draw(mouse_pos, window)
    if hover_little or tasks:
        render.render(window)
        hover_button = False
        if not tasks:
            hover_button = render.tasks_button.draw(mouse_pos, window)
        if hover_button and mouse_click:
            render.render(window)
            tasks = True
        if mouse_click:
            render.render(window)
            tasks = False
    return tasks
    # while tasks:
    #     render.tasks_tab(window)
    # if hover_little: # and not tasks:
    #     render.render(window)
    #     hover_button = render.tasks_button.draw(mouse_pos, window)