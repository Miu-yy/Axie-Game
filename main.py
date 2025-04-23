#import pygame.time
import pygame

from sprites import *
#from render import *
#from interactable import *
from ui import ui
from ui import tasks
#import ui
from draw import render
from state import *

sprites = pygame.image.load("assets/sprites/sprites-32x32.png")
sprites = pygame.transform.scale_by(sprites, 4)
rect = pygame.Rect(0, 0, 60, 60)
image = sprites.subsurface(rect)

window = pygame.display.set_mode((512,256))
clock = pygame.time.Clock()

pygame.display.set_caption('Axie Game')
pygame.display.set_icon(image)

MENU_QUIT = pygame.USEREVENT + 1

class Input():
    def __init__(self):
        self.state = State()
        self.running = self.state.running
        self.player = self.state.player

        # TEMP
        self.state.load_save_game()
        self.player.task_pages()
        # TEMP

        self.mouse_move = False
        self.mouse_click = False
        self.mouse_pos = (0,0)
        self.mouse_button = 0
        self.key_input = ''
        self.backspace = False
        self.enter = False
        self.is_digit = False

        self.task_title_received = False
        self.task_value_received = False
        self.task_title = ''
        self.task_value = ''


        self.hover_little = False
        self.hover_button = False

        self.tasks = False
        self.buy = False
        self.place = False
        self.game_state = self.state.state

        self.tasks_menu = tasks.Tasks(self.player)



    def process_input(self):
        pass
        # if self.tasks:
        #     render.tasks_tab(window)
        #tasks()
               # if self.hover_little:
        #     if self.hover_button and self.mouse_click:
        #         self.tasks = True
        # else:
        #     pass

    def get_input(self):
        while self.running:
            render.render(window)
            #self.tasks = tasks.render_tasks(window, self.tasks, self.mouse_pos, self.mouse_click)
            if self.tasks:
                pass
               # ui.tasks.render.tasks_tab(window)
            # self.hover_little = render.tasks_little.draw(self.mouse_pos, window)
            # if self.hover_little and not self.tasks:
            #     render.render(window)
            #     self.hover_button = render.tasks_button.draw(self.mouse_pos, window)
            # if self.tasks:
            #     render.tasks_tab(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                    self.mouse_move = True
                    #tasks = tasksLittle.draw(mouse_pos, window)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = event.pos
                    self.mouse_button = event.button
                    self.mouse_click = True
                self.process_input()
            pygame.display.update()
            clock.tick(60)
            print("?")

    def update_state(self):
        if self.tasks:
            self.state.tasks_menu = True
        elif self.buy:
            self.state.buy_menu = True
        elif self.place:
            self.state.placing_overlay = True

        self.state.update_state()
        self.game_state = self.state.state
        #print(self.player.num_pages())
        #print(self.player.num_tasks())


        if self.state.tasks_menu:
            if not self.tasks_menu.render_tasks_tab(window,self.mouse_pos,self.mouse_click):
                self.state.tasks_menu = False
                pygame.event.post(pygame.event.Event(MENU_QUIT))
            if self.player.adding_task:
                self.task_title_received = self.player.get_text_input(self.key_input,self.backspace,self.enter)
                self.backspace = False
                if self.task_title_received:
                    self.task_title = self.player.player_text
                    self.player.player_text = ''
                    self.enter = False
            if self.player.adding_value:
                if self.is_digit or self.backspace or self.enter:
                    self.task_value_received = self.player.get_text_input(self.key_input,self.backspace,self.enter)
                    self.backspace = False
                    if self.task_value_received:
                        self.task_value = self.tasks_menu.new_task_value
                        self.player.player_text = ''
                        self.enter = False
            self.key_input = ''
            if self.task_title_received and self.task_value_received:
                self.task_title_received = False
                self.task_value_received = False
                self.player.add_task(self.task_title,self.task_value)
                self.player.task_pages()

    def process_event(self):
        self.tasks,self.buy,self.place = render.render(window,self.mouse_pos,self.mouse_click,self.player.points)

    def game_loop(self):
        while self.running:
            self.mouse_move = False
            self.mouse_click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state.write_save_game()
                    self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                    self.mouse_move = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = event.pos
                    self.mouse_button = event.button
                    self.mouse_click = True
                if event.type == pygame.KEYDOWN:
                    self.key_input = event.unicode
                    self.is_digit = event.unicode.isdigit()
                    if event.type == pygame.K_BACKSPACE:
                        self.backspace = True
                    if event.key == pygame.K_RETURN:
                        self.enter = True

                self.process_event()
            self.update_state()
            #render.render_state(window,self.game_state)

            pygame.display.update()
            clock.tick(60)


    def run(self):
        while self.running:
            self.game_loop()


play = Input()
play.run()

print(Player)

pygame.quit()

# sprites = pygame.image.load("sprites-32x32.png")
# sprites = pygame.transform.scale_by(sprites, 8)
# moLocation = pygame.math.Vector2(32,32)
# moSprite = pygame.Rect(0,0,152,48)
# #window.blit(sprites,moLocation,moSprite)
# stumpLocation = pygame.math.Vector2(256,176)
# stumpSprite = pygame.Rect(0,64,152,48)
# #window.blit(sprites,stumpLocation,stumpSprite)

