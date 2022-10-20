from pico2d import *
import character
import background
import os

ix = 600
iy = 450
os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
state = character
state.open_canvas(state.TUK_WIDTH, state.TUK_HEIGHT)
background.enter()


state.enter()
while(state.running):
    state.handle_events()
    clear_canvas()
    background.update()
    state.update()
    state.draw()
    update_canvas()  
    delay(0.016)
