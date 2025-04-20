#import pygame.time
from sprites import *
#from render import *
#from interactable import *
from ui import tasks
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

class Input():
    def __init__(self):
        self.state = State()
        self.running = self.state.running

        # TEMP
        self.state.load_save_game()
        self.state.player.update_points(5)
        self.state.player.add_task("task2",3,False)
        self.state.player.add_task("task3",5,True)
        print(self.state.player.tasks,"/",self.state.player.points)
        # TEMP

        self.mouse_move = False
        self.mouse_click = False
        self.mouse_pos = (0,0)
        self.mouse_button = 0

        self.hover_little = False
        self.hover_button = False

        self.tasks = False
        self.buy = False
        self.place = False
        self.game_state = self.state.state


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
            self.tasks = tasks.render_tasks(window, self.tasks, self.mouse_pos, self.mouse_click)
            if self.tasks:
                render.tasks_tab(window)
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

    def update_state(self):
        if self.tasks:
            self.state.tasks_menu = True
        elif self.buy:
            self.state.buy_menu = True
        elif self.place:
            self.state.placing_overlay = True

        self.state.update_state()
        self.game_state = self.state.state
        print(self.game_state)

        if self.state.tasks_menu:
            tasks.render_tasks_tab(window,self.state.player.tasks)
            # num_tasks = 0
            # for task in self.state.player.tasks:
            #     num_tasks += 1
            #     y = 32 + 16*num_tasks


        #
        # if self.state.buy_menu:
        #     render.tasks_tab(window)
        #

        # if self.state.placing_overlay:
        #     render.tasks_tab(window)

    def process_event(self):
        self.tasks,self.buy,self.place = render.render(window,self.mouse_pos,self.mouse_click)

    def game_loop(self):
        while self.running:
            self.mouse_move = False
            self.mouse_click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.mouse_pos = event.pos
                    self.mouse_move = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pos = event.pos
                    self.mouse_button = event.button
                    self.mouse_click = True
                self.process_event()
            self.update_state()
            render.render_state(window,self.game_state)

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

