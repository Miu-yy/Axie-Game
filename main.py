import pygame
from sprites import *
import tasks

window = pygame.display.set_mode((512,256))
tasks = tasks.tasks

# Import background
tank = pygame.image.load("tank-32x32.png")
tank = pygame.transform.scale_by(tank,16)

# Draw background
tankLocation = pygame.math.Vector2(0,0)
tankSprite = pygame.Rect(0,256,512,256)
window.blit(tank,tankLocation,tankSprite)

# Groups
mo = pygame.sprite.GroupSingle()
mo.add(Mo())
stumpy = pygame.sprite.GroupSingle()
stumpy.add(Stumpy())
decorations = pygame.sprite.Group()
decorations.add(Decorations('log',2))

running = True
while running:
    mo.draw(window)
    stumpy.draw(window)
    decorations.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.update()

pygame.quit()

# sprites = pygame.image.load("sprites-32x32.png")
# sprites = pygame.transform.scale_by(sprites, 8)
# moLocation = pygame.math.Vector2(32,32)
# moSprite = pygame.Rect(0,0,152,48)
# #window.blit(sprites,moLocation,moSprite)
# stumpLocation = pygame.math.Vector2(256,176)
# stumpSprite = pygame.Rect(0,64,152,48)
# #window.blit(sprites,stumpLocation,stumpSprite)

