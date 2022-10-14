from pico2d import *
import character

state = character

state.open_canvas(state.TUK_WIDTH, state.TUK_HEIGHT)
state.enter()

while(state.running):
    state.handle_events()
    clear_canvas()
    state.hero.update()
    state.hero.draw()
    update_canvas()
