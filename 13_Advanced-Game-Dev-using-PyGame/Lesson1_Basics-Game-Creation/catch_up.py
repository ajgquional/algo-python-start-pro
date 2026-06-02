from pygame import *

# fix if the sprites cannot be found even if it is in the same folder as the script
# this happens when the terminal does not point specifically to the folder where the script is located, but to a parent folder
from pathlib import Path
script_dir = Path(__file__).resolve().parent

# create game window
window = display.set_mode((700, 500))
display.set_caption("catch")

# set scene background
background = transform.scale(image.load(script_dir / "background.png"), (700, 500))
# use background = transform.scale(image.load("background.png"), (700, 500)) if terminal points to the folder where the script is located

# parameters of the image sprite
x1 = 100
y1 = 300

x2 = 300
y2 = 300

# creating 2 sprites and placing them on the scene
sprite1 = transform.scale(image.load(script_dir / "sprite1.png"), (100, 100))
# use sprite1 = transform.scale(image.load("sprite1.png"), (100, 100)) if terminal points to the folder where the script is located
sprite2 = transform.scale(image.load(script_dir / "sprite2.png"), (100, 100))
# use sprite2 = transform.scale(image.load("sprite2.png"), (100, 100)) if terminal points to the folder where the script is located
speed = 10

# game loop
run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    # handling click and close window event 
    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    display.update()
    clock.tick(FPS)
