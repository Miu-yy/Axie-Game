from sprites import *
#from render import *
#from interactable import *
from ui import tasks
from draw import render
from game_save import *

window = pygame.display.set_mode((512,256))

# Extract save data
backup_save_data = load_save("save")
game_data = load_save("save")

class Input():
    def __init__(self):
        self.running = True

        self.mouse_move = False
        self.mouse_click = False
        self.mouse_pos = (0,0)
        self.mouse_button = 0

        self.hover_little = False
        self.hover_button = False

        self.tasks = False


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

    def run(self):
        while self.running:
            self.get_input()

print(backup_save_data)

play = Input()
play.run()

pygame.quit()

# sprites = pygame.image.load("sprites-32x32.png")
# sprites = pygame.transform.scale_by(sprites, 8)
# moLocation = pygame.math.Vector2(32,32)
# moSprite = pygame.Rect(0,0,152,48)
# #window.blit(sprites,moLocation,moSprite)
# stumpLocation = pygame.math.Vector2(256,176)
# stumpSprite = pygame.Rect(0,64,152,48)
# #window.blit(sprites,stumpLocation,stumpSprite)

