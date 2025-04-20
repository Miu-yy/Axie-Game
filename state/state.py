from game_save import *
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
        self.tasks = []
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

    def add_task(self,title,value,completed):
        task = {"title": title,
                 "value": value,
                 "completed": completed}
        self.tasks.append(task)


    def remove_task(self):
        pass

    def complete_task(self):
        pass

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

