from pico2d import *
import character
import background
import enemy
import os

ix = 600
iy = 450
os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
open_canvas(character.TUK_WIDTH, character.TUK_HEIGHT)
background.enter()
running = None

def handle_events():
    global running
    character.handle_events()


def enter():
    global running
    running = True
    character.enter()
    background.enter()
    enemy.enter()

def draw():
    background.update()
    character.draw()
    enemy.draw()

def update():
    character.update()
    enemy.update()

enter()
while(running):
    handle_events()
    clear_canvas()
    draw()
    update()
    update_canvas()  
    delay(0.016)
