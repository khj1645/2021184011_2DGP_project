from pico2d import *
import character
import os

os.chdir('d:\\2021184011_2DGP_project\\Sprite_use')
state = character
state.open_canvas(state.TUK_WIDTH, state.TUK_HEIGHT)
state.enter()
while(state.running):
    state.handle_events()
    clear_canvas()
    image = load_image('Land1DecoA.png')
    image.clip_draw(0, 0, 1200, 900, 600, 450, 1200, 900)
    state.update()
    state.draw()
    update_canvas()  
    delay(0.016)
