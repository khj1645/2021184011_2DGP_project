from pico2d import *
import character
import rect
import os

ix = 600
iy = 450
os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
state = character
state.open_canvas(state.TUK_WIDTH, state.TUK_HEIGHT)
backgrounds = load_image('Land1DecoA.png')

background_pos = []

for i in range(0,9):
    background_pos.append(rect.rect())
    
    background_pos[i].x  = 100 + (i%3) * 2000
    background_pos[i].y  = -50 + (i//3) * 2000
    background_pos[i].rx = background_pos[i].ry = 1000


state.enter()
while(state.running):
    state.handle_events()
    clear_canvas()

    for i in range(0,9):
        background_pos[i].x -= state.hero.unit_x
        background_pos[i].y -= state.hero.unit_y
        background_pos[i].update()
        backgrounds.clip_draw(0, 0, 500, 500, background_pos[i].x, background_pos[i].y, 2000, 2000)

    for i in range(0,9):
        if background_pos[i].right < 0:
            background_pos[i].x += 4000
        elif background_pos[i].left > 1200:
            background_pos[i].x -= 4000
        elif background_pos[i].top < 0:
            background_pos[i].y += 4000
        elif background_pos[i].bottom > 900:
            background_pos[i].y -= 4000
        background_pos[i].update()
    state.update()
    state.draw()
    update_canvas()  
    delay(0.016)
