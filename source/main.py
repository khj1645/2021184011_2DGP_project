from pico2d import *
import character
import background
import enemy
import game_framework

running = None

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_events(event)


def enter():
    global running
    running = True
    character.enter()
    background.enter()
    enemy.enter()

def exit():
    pass

def draw():
    clear_canvas()
    background.update()
    character.draw()
    enemy.draw()
    update_canvas()

def update():
    character.update()
    enemy.update()
    delay(0.016)

def pause():
    pass

def resume():
    pass
# enter()
# while(running):
#     handle_events()
#     clear_canvas()
#     draw()
#     update()
#     update_canvas()  
#     delay(0.016)
