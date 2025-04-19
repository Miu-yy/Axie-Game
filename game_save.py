import json
import pygame

#folder = pygame.system.get_pref_path("Miu_yy","Axie-Game")
folder = "C:\\Users\\Miuwai\\Documents\\Git\\Axie-Game\\data\\"
print(folder)

def load_save(filename):
    filepath = folder + filename + ".json"
    with open(filepath,'r') as loaded_file:
        return json.load(loaded_file)

def write_save(filename,data):
    filepath = folder + filename + ".json"
    with open(filepath,'w') as output_file:
        json.dump(data,output_file,indent=2)

#data = load_save("save")

# data = {
#   "log": 0,
#   "rock": 0,
#   "weed": 0,
#   "flower": 0
# }
#
# print(type(data))
# write_save("decorations",data)