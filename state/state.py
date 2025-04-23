from game_save import *
import math, time
# player and object state

class State():
    def __init__(self):
        self.running = True
        self.player = Player()

        self.tasks_menu = False
        self.buy_menu = False
        self.placing_overlay = False
        self.state = [self.tasks_menu,self.buy_menu,self.placing_overlay]

        self.load_save_game()
        self.backup_save_data = load_save("save")
        # game_data = load_save("save")

    def load_save_game(self):
        save_data = load_save("save")
        self.player.points = save_data.get("points",0)
        self.player.tasks = save_data.get("tasks",[])
        self.player.owned_decorations = save_data.get("owned_decorations",[{"item": "weed", "level": 0}])
        self.player.placed_decorations = save_data.get("placed_decorations",[])

    def update_state(self):
        self.state = [self.tasks_menu,self.buy_menu,self.placing_overlay]


class Player():
    def __init__(self):
        self.points = 0
        self.player_text = ''
        self.tasks = []
        self.pages = []
        self.owned_decorations = []
        self.placed_decorations = []

    def update_points(self,points_value): # points_value can be positive (earned points), or negative (spent points)
        points = self.points
        points += points_value
        if points > 0:
            self.points = points # If can afford, action successful
            return True
        else:
            return False

    def num_tasks(self):
        return len(self.tasks)


    def num_pages(self):
        return math.ceil(self.num_tasks()/8)

    def get_text_input(self,key_input):
        self.player_text += key_input
        print(self.player_text)

    def add_task(self,title,value,completed=False):
        num = self.num_tasks()
        task = {"number": num+1,
                 "title": title,
                 "value": value,
                 "completed": completed}
        self.tasks.append(task)


    def remove_task(self,number):
        removed = False
        index = -1
        for index,task in enumerate(self.tasks):
            if task["number"] == number:
                self.tasks.remove(task)
                removed = True
                break
        if removed:
            for i,task in enumerate(self.tasks):
                if i >= index:
                    task["number"] -= 1


    def complete_task(self,number):
        for task in self.tasks:
            if task["number"] == number:
                task["completed"] = not task["completed"]
                self.update_points(task["value"])


    def task_pages(self):
        self.pages = []
        x = 0
        page = []
        for task in self.tasks:
            page.append(task)
            x += 1
            if x%8 == 0:
                self.pages.append(page)
                page = []
                x = 0
        self.pages.append(page)


    def decoration_bought(self): # Or upgraded
        pass

    def decoration_placed(self):
        pass



class Object():
    def __init__(self):
        self.x
        self.y

class Decoration(Object):
    def __init__(self):
        super().__init__()
        self.level
        self.unlocked
        self.placed

class Axie(Object):
    def __init__(self):
        super().__init__()
        self.momentum
        self.unlocked

class Food(Object):
    def __init__(self):
        super().__init__()
        self.momentum


class Bubble(Object):
    def __init__(self):
        super().__init__()
        self.momentum

