#import pygame.time
import pygame
from PIL.ImageChops import screen

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

min_width = 512
min_height = 256
max_width = 1024
max_height = 512
aspect_ratio = 512/256

window = pygame.display.set_mode((512,256),pygame.RESIZABLE)
clock = pygame.time.Clock()

pygame.display.set_caption('Axie Game')
pygame.display.set_icon(image)

# Custom events
MENU_QUIT = pygame.USEREVENT + 1
POINTS_UPDATED = pygame.USEREVENT + 2
TASK_REMOVED = pygame.USEREVENT + 3


class Input():
    def __init__(self):
        self.window = window
        self.screen = pygame.Surface((512,256))

        self.width = min_width
        self.height = min_height

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
            if not self.tasks_menu.render_tasks_tab(self.screen,self.mouse_pos,self.mouse_click):
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
        self.tasks,self.buy,self.place = render.render(self.screen,self.mouse_pos,self.mouse_click,self.player.points)

    def game_loop(self):
        while self.running:
            self.mouse_move = False
            self.mouse_click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state.write_save_game()
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    if event.w < min_width:
                        self.width = min_width
                    elif event.w > max_width:
                        self.width = max_width
                    else:
                        self.width = event.w
                    if event.h < min_height:
                        self.height = min_height
                    elif event.h > max_height:
                        self.height = max_height
                    else:
                        self.height = event.h
                    if event.w/event.h != aspect_ratio:
                        self.height = self.width/2
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                    # self.mouse_pos[0] = self.mouse_pos[0]/self.width*512
                    # self.mouse_pos[1] = self.mouse_pos[1]/self.height*256
                    # self.mouse_pos = tuple(self.mouse_pos)
                    self.mouse_move = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = event.pos
                    # self.mouse_pos[0] = self.mouse_pos[0]/self.width*512
                    # self.mouse_pos[1] = self.mouse_pos[1]/self.height*256
                    # self.mouse_pos = tuple(self.mouse_pos)
                    self.mouse_button = event.button
                    self.mouse_click = True
                if event.type == pygame.KEYDOWN:
                    self.key_input = event.unicode
                    self.is_digit = event.unicode.isdigit()
                    if event.type == pygame.K_BACKSPACE:
                        self.backspace = True
                    if event.key == pygame.K_RETURN:
                        self.enter = True
                self.mouse_pos = list(self.mouse_pos)
                self.mouse_pos[0] = self.mouse_pos[0] / self.width * 512
                self.mouse_pos[1] = self.mouse_pos[1] / self.height * 256
                self.mouse_pos = tuple(self.mouse_pos)
                self.process_event()
            self.update_state()
            self.window.blit(pygame.transform.scale(self.screen,(self.width,self.height)))
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

