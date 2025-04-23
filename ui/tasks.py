import pygame
from state import *
from render import *
from button import *
from ui import ui
import math

# Import tasks
view_tasks = pygame.image.load("assets/ui/tasksmenu-32x32.png")
view_tasks = pygame.transform.scale_by(view_tasks,7)
tasks_rect = pygame.Rect(16,16,224,224)

# Create checkbox buttons
# checkboxes = []
# for i in range(8):
#     x = 37 + (7*(i>3)) + (7*(i>5))
#     y = 44 + 21*i
#     checkboxes.append(Button("assets/ui/checkbox-32x32.png", 1, x, y, 16, 16))

def task_pos(number):
    x_pos = 37 + (7 * (number > 3)) + (7 * (number > 5))
    y_pos = 44 + 21 * number
    return x_pos,y_pos

#checked_checkbox = Button("assets/ui/checkedbox-32x32.png", 1, 0, 0, 16, 16)

# Create arrow buttons
down_arrow = Button("assets/ui/arrow-32x32.png", 1, 203, 213.5, 16, 16)
up_arrow = Button("assets/ui/uparrow-32x32.png", 1, 189, 33.5, 16, 16)

# Create add button
add = Button("assets/ui/plus-32x32.png", 0.7,182, 210, 16, 16)

# Create exit screen button
cross = Button("assets/ui/cross-32x32.png", 0.7,226, 16, 16, 16)


#tasks_menu = ui.Ui(self.player)

class Tasks(ui.Ui):
    def __init__(self,player):
        super().__init__(player)
        self.player = player

        self.tasks = self.player.tasks
        self.num_tasks = self.player.num_tasks()
        self.num_pages = self.player.num_pages()
        self.page = 0
        self.pages = self.player.pages
        self.checkboxes = []

        # Temp for rendering
        self.new_task_text = ''
        self.new_task_value = ''

    def task_page(self,window):
        pass
        # if self.page == 1:
        #     if down_arrow.draw(window):
        #         self.page += 1
        # elif self.page == self.num_pages:
        #     if up_arrow.draw(window):
        #         self.page += 1
        # else:
        #     if down_arrow.draw(window):
        #         self.page += 1
        #     elif up_arrow.draw(window):
        #         self.page -= 1

    def create_checkboxes(self):
        m = 0
        for n in range(self.num_pages):
            page = []
            for i in range(8):
                x, y = task_pos(i)
                page.append(Button("assets/ui/checkbox-32x32.png", 1, x, y, 16, 16))
                m += 1
                # if m == self.num_tasks:
                #     break
            self.checkboxes.append(page)

    def add_task(self,keyboard):
        pass

    def render_tasks_tab(self,window,mouse_pos,mouse_click):
        # Render menu
        window.blit(view_tasks,tasks_rect)

        # Exit button
        if cross.draw_click(window,mouse_pos,mouse_click):
            return False

        # Re-initialise
        self.player.task_pages()
        self.pages = self.player.pages
        self.num_tasks = self.player.num_tasks()
        self.num_pages = self.player.num_pages()


        # List tasks with checkboxes
        self.create_checkboxes()
        n = 0
        for task in self.pages[self.page]:
            if not task["completed"]:
                if self.checkboxes[self.page][n].draw_click(window,mouse_pos,mouse_click):
                    self.player.complete_task(task["number"])
                    task["completed"] = True
                    break
                x,y = task_pos(n)
                render_font(window, (0,0,0),(230,212,179), task["title"], 21, x+21, y-2)
                render_font(window, (0,255,0),(230,212,179), str(task["value"]), 20, x+147, y)
            elif task ["completed"]:
                self.checkboxes[self.page][n].change_image("assets/ui/checkedbox-32x32.png")
                if self.checkboxes[self.page][n].draw_click(window,mouse_pos,mouse_click):
                    self.player.complete_task(task["number"])
                    task["completed"] = False
                    self.checkboxes[self.page][n].change_image("assets/ui/checkbox-32x32.png")
                    break
                x,y = task_pos(n)
                render_font(window, (0,0,0),(230,212,179), task["title"], 21, x+21, y-2)
                render_font(window, (0,255,0),(230,212,179), str(task["value"]), 20, x+147, y)
            n+=1
            if n==8 or n==self.num_tasks:
                break

        # Arrow buttons for changing page
        if self.page < self.num_pages-1 or n==8:
            if down_arrow.draw_click(window, mouse_pos, mouse_click):
                self.page += 1
        if self.page > 0:
            if up_arrow.draw_click(window,mouse_pos,mouse_click):
                self.page -= 1
        if self.page == self.num_pages-1:
            if add.draw_click(window, mouse_pos, mouse_click):
                self.player.adding_task = True

        # Text input for adding a task
        x,y = task_pos(n)
        if self.player.adding_task:
            self.checkboxes[self.page][n].draw_click(window,mouse_pos,mouse_click)
            self.new_task_text = self.player.player_text
            render_font(window, (0,0,0),(230,212,179), self.new_task_text, 21, x+21, y-2)
        if self.player.adding_value:
            self.checkboxes[self.page][n].draw_click(window,mouse_pos,mouse_click)
            self.new_task_value = self.player.player_text
            render_font(window, (0, 0, 0),(230,212,179), self.new_task_text, 21, x + 21, y - 2)
            render_font(window, (0,255,0),(230,212,179), self.new_task_value, 20, x+147, y)


        return True

        # if self.page == self.num_pages:
        #     if add.draw_click(window, mouse_pos, mouse_click):
        #         self.player.adding_task = True