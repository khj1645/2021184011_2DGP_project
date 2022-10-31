from pico2d import *
import character
import background
import enemy
import os

ix = 600
iy = 450
os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
open_canvas(character.TUK_WIDTH, character.TUK_HEIGHT - 150)
background.enter()
running = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            character.handle_events(event)


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
