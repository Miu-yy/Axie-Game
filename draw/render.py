from sprites import *
import button

# Import background
tank = pygame.image.load("assets/background/tank-32x32.png")
tank = pygame.transform.scale_by(tank,16)

# Create main buttons
tasks_icon = button.Button("assets/ui/tasks-32x32.png", 1, 16, 16, 32, 19)
tasks_button = button.Button("assets/ui/tasks-32x32.png", 4, 16, 16, 128, 76)

buy_icon = button.Button("assets/ui/tasks-32x32.png", 1, 16, 48, 32, 19)
buy_button = button.Button("assets/ui/tasks-32x32.png", 4, 16, 48, 128, 76)

place_icon = button.Button("assets/ui/tasks-32x32.png", 1, 16, 80, 32, 19)
place_button = button.Button("assets/ui/tasks-32x32.png", 4, 16, 80, 128, 76)



# Draw background
def background(window):
    location = pygame.math.Vector2(0,0)
    sprite = pygame.Rect(0,256,512,256)
    window.blit(tank,location,sprite)

def buttons(window,icon,button,mouse_position,mouse_click):
    icon.draw_hover(window,mouse_position)
    if icon.hover:
        if button.draw_hover(window,mouse_position):
            background(window)
            if button.draw_hover(window,mouse_position) and mouse_click:
                background(window)
                return True
        else:
            icon.hover = False
    return False

def render(window,mouse_position,mouse_click):
    background(window)
    tasks = buttons(window,tasks_icon,tasks_button,mouse_position,mouse_click)
    buy = buttons(window,buy_icon,buy_button,mouse_position,mouse_click)
    place = buttons(window,place_icon,place_button,mouse_position,mouse_click)
    mo.draw(window)
    stumpy.draw(window)
    decorations.draw(window)

    return tasks,buy,place


def render_font(window,colour,text,size,x,y):
    pygame.font.init()
    font = pygame.font.Font('assets/fonts/MedodicaRegular.otf', size)
    disp_text = pygame.font.Font.render(font, text, True, colour,(230,212,179))
    window.blit(disp_text,(x, y))

def render_state(window,state):
    if state[0]:
        pass
    elif state[1]:
        pass
    elif state[2]:
        pass

# Groups


# Buttons

#tasksButton.draw(window)