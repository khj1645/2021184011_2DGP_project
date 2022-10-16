from pico2d import *
import character

state = character
state.open_canvas(state.TUK_WIDTH, state.TUK_HEIGHT)
state.enter()
while(state.running):
    state.handle_events()
    clear_canvas()
    image = load_image('Land1DecoA.png')
    image.clip_draw(0, 0, 1200, 900, 600, 450, 1200, 900)
    state.hero.update()
    state.hero.draw()
    update_canvas()  
    delay(0.016)
