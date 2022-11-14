from pico2d import *
import character
import background
import enemy
import game_framework
import lobby
import item
running = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(lobby)
        else:
            character.handle_events(event)


def enter():
    global running
    running = True
    character.enter()
    background.enter()
    enemy.enter()
    item.enter()

def exit():
    pass

def draw():
    clear_canvas()
    background.draw()
    enemy.draw()
    item.draw()
    character.draw()
    update_canvas()

def update():
    background.update()
    character.update()
    enemy.update()
    item.update()
    delay(0.016)

def pause():
    pass

def resume():
    pass
